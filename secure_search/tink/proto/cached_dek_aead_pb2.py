# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tink/proto/cached_dek_aead.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tink/proto/cached_dek_aead.proto',
  package='google.crypto.tink',
  syntax='proto3',
  serialized_options=b'\n\034com.google.crypto.tink.protoP\001Z5github.com/google/tink/proto/cached_dek_aead_go_proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n tink/proto/cached_dek_aead.proto\x12\x12google.crypto.tink\")\n\x16\x43\x61\x63hedDekAeadKeyFormat\x12\x0f\n\x07key_uri\x18\x01 \x01(\t\"_\n\x10\x43\x61\x63hedDekAeadKey\x12\x0f\n\x07version\x18\x01 \x01(\r\x12:\n\x06params\x18\x02 \x01(\x0b\x32*.google.crypto.tink.CachedDekAeadKeyFormatBW\n\x1c\x63om.google.crypto.tink.protoP\x01Z5github.com/google/tink/proto/cached_dek_aead_go_protob\x06proto3'
)




_CACHEDDEKAEADKEYFORMAT = _descriptor.Descriptor(
  name='CachedDekAeadKeyFormat',
  full_name='google.crypto.tink.CachedDekAeadKeyFormat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_uri', full_name='google.crypto.tink.CachedDekAeadKeyFormat.key_uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=97,
)


_CACHEDDEKAEADKEY = _descriptor.Descriptor(
  name='CachedDekAeadKey',
  full_name='google.crypto.tink.CachedDekAeadKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='google.crypto.tink.CachedDekAeadKey.version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='params', full_name='google.crypto.tink.CachedDekAeadKey.params', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=194,
)

_CACHEDDEKAEADKEY.fields_by_name['params'].message_type = _CACHEDDEKAEADKEYFORMAT
DESCRIPTOR.message_types_by_name['CachedDekAeadKeyFormat'] = _CACHEDDEKAEADKEYFORMAT
DESCRIPTOR.message_types_by_name['CachedDekAeadKey'] = _CACHEDDEKAEADKEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CachedDekAeadKeyFormat = _reflection.GeneratedProtocolMessageType('CachedDekAeadKeyFormat', (_message.Message,), {
  'DESCRIPTOR' : _CACHEDDEKAEADKEYFORMAT,
  '__module__' : 'tink.proto.cached_dek_aead_pb2'
  # @@protoc_insertion_point(class_scope:google.crypto.tink.CachedDekAeadKeyFormat)
  })
_sym_db.RegisterMessage(CachedDekAeadKeyFormat)

CachedDekAeadKey = _reflection.GeneratedProtocolMessageType('CachedDekAeadKey', (_message.Message,), {
  'DESCRIPTOR' : _CACHEDDEKAEADKEY,
  '__module__' : 'tink.proto.cached_dek_aead_pb2'
  # @@protoc_insertion_point(class_scope:google.crypto.tink.CachedDekAeadKey)
  })
_sym_db.RegisterMessage(CachedDekAeadKey)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
