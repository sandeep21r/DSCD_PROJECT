import grpc
import process_pb2 as pb2
import process_pb2_grpc as pb2_grpc
from concurrent import futures
import random

class ReducerImplementation(pb2_grpc.MasterMapperServicer):
    def __init__(self, reducer_id):
        self.reducer_id = reducer_id
        self.dict_centroid = {}

    def GetReducerDetails(self, request, context):
        print("Received request")
        num_reducers = request.numReducers
        print("Number of reducers:", num_reducers)
        print("Reducer ID:", self.reducer_id)

        num_mappers = request.numMappers
        partition_id = request.partition_id
        lines=[]
        for i in range(num_mappers):
            try:
                channel = grpc.insecure_channel(f"localhost:5005{i+1}")
                stub = pb2_grpc.MasterMapperStub(channel)
                request = pb2.GetInputRequest(reducer_id=partition_id)
                response = stub.GetInputfromMapper(request)
                lines.extend(response.data.split("\n"))
            except grpc._channel._InactiveRpcError:
                print(f"Error in processing points by mapper {i + 1}")

            except Exception as e:
                print(f"Error in processing points by mapper {i + 1}")

        # print("Data received from mappers:", lines)
        self.shuffle_and_sort(lines)
        data=""
        for line in open(f"Reducers/R{reducer_id}.txt", 'r'):
            data += line
        # prob=random.random()
        # if prob<0.5:
        #     return pb2.MapPartitionResponse(status="Failure")
        return pb2.ReduceResponse(status="Success", data=data)
        

    def shuffle_and_sort(self, lines):
        self.dict_centroid = {}
        lines=lines[:-1]
        print("Shuffled and sorted data:", self.dict_centroid)
        # print(lines)
        for line in lines:
            print(line)
            if line == "":
                continue
            centroid_index,point_x,point_y = line.strip().split(" ")
            print(centroid_index,point_x,point_y)

            if(centroid_index not in self.dict_centroid):
                self.dict_centroid[centroid_index]=[]
            
            self.dict_centroid[centroid_index].append([point_x,point_y])

        print("Shuffled and sorted data:", self.dict_centroid)
        for centroid_index, points in self.dict_centroid.items():
            points.sort(key=lambda x: (float(x[0]), float(x[1])))
        dict_centroid = dict(sorted(self.dict_centroid.items(), key=lambda x: x[0]))
       
        self.Reduce()
        print("Shuffled and sorted data:", self.dict_centroid)

    def Reduce(self):
        updated_centroids = {}
        for centroid_index, points in self.dict_centroid.items():
            if not points:
                continue
            
            sum_x = sum(float(point[0]) for point in points)
            sum_y = sum(float(point[1]) for point in points)
            num_points = len(points)
            new_centroid_x = round((sum_x / num_points),20)
            new_centroid_y = round((sum_y / num_points),20)
            
            updated_centroids[centroid_index] = [new_centroid_x, new_centroid_y]
    

        print("Shuffled and sorted data:", self.dict_centroid)


        print("Updated centroids:", updated_centroids)
        with open(f"Reducers/R{self.reducer_id}.txt", 'w') as file:
            for centroid_index, centroid in updated_centroids.items():
                file.write(f"{centroid_index} {centroid[0]} {centroid[1]}\n")   


if __name__ == "__main__":

    reducer_id = int(input("Enter reducer id: "))
    reducer_ips = {1: "localhost:50061", 2: "localhost:50062", 3: "localhost:50063"}
    port = int(reducer_ips[reducer_id].split(":")[1])
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    reducer_impl = ReducerImplementation(reducer_id)
    pb2_grpc.add_MasterMapperServicer_to_server(reducer_impl, server)
    print("Server started on port:", port)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    server.wait_for_termination()
