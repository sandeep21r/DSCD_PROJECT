# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: notification_server.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19notification_server.proto\"\xa7\x01\n\x05Items\x12\x0f\n\x07item_id\x18\x01 \x01(\t\x12\x14\n\x0cproduct_name\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\t\x12\x10\n\x08quantity\x18\x04 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x16\n\x0eseller_address\x18\x06 \x01(\t\x12\x16\n\x0eprice_per_unit\x18\x07 \x01(\x02\x12\x0e\n\x06rating\x18\x08 \x01(\x02\" \n\rItemsResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2D\n\x13NotificationService\x12-\n\x13ReceiveNotification\x12\x06.Items\x1a\x0e.ItemsResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'notification_server_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ITEMS']._serialized_start=30
  _globals['_ITEMS']._serialized_end=197
  _globals['_ITEMSRESPONSE']._serialized_start=199
  _globals['_ITEMSRESPONSE']._serialized_end=231
  _globals['_NOTIFICATIONSERVICE']._serialized_start=233
  _globals['_NOTIFICATIONSERVICE']._serialized_end=301
# @@protoc_insertion_point(module_scope)
