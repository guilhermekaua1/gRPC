# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nchat.proto\x12\x04\x63hat\"\x07\n\x05\x45mpty\"\x1c\n\x08\x43hatUser\x12\x10\n\x08username\x18\x01 \x01(\t\"0\n\x0b\x43hatMessage\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t2\x94\x01\n\x04\x43hat\x12)\n\x07\x63onnect\x12\x0e.chat.ChatUser\x1a\x0e.chat.ChatUser\x12.\n\x0csend_message\x12\x11.chat.ChatMessage\x1a\x0b.chat.Empty\x12\x31\n\x0freceive_message\x12\x0b.chat.Empty\x1a\x11.chat.ChatMessageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chat_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EMPTY']._serialized_start=20
  _globals['_EMPTY']._serialized_end=27
  _globals['_CHATUSER']._serialized_start=29
  _globals['_CHATUSER']._serialized_end=57
  _globals['_CHATMESSAGE']._serialized_start=59
  _globals['_CHATMESSAGE']._serialized_end=107
  _globals['_CHAT']._serialized_start=110
  _globals['_CHAT']._serialized_end=258
# @@protoc_insertion_point(module_scope)
