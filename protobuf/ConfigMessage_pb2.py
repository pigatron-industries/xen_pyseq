# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ConfigMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ConfigMessage.proto',
  package='xen',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x13\x43onfigMessage.proto\x12\x03xen\"U\n\rConfigWrapper\x12)\n\rchannelConfig\x18\x01 \x01(\x0b\x32\x12.xen.ChannelConfig\x12\x19\n\x05scale\x18\x02 \x01(\x0b\x32\n.xen.Scale\"<\n\rChannelConfig\x12+\n\x0e\x63hannelMapping\x18\x01 \x03(\x0b\x32\x13.xen.ChannelMapping\"Q\n\x0e\x43hannelMapping\x12\x13\n\x0bmidiChannel\x18\x01 \x02(\x05\x12\x15\n\rcvChannelFrom\x18\x02 \x02(\x05\x12\x13\n\x0b\x63vChannelTo\x18\x03 \x02(\x05\"\x16\n\x05Scale\x12\r\n\x05\x63\x65nts\x18\x01 \x03(\x05')
)




_CONFIGWRAPPER = _descriptor.Descriptor(
  name='ConfigWrapper',
  full_name='xen.ConfigWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channelConfig', full_name='xen.ConfigWrapper.channelConfig', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale', full_name='xen.ConfigWrapper.scale', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=113,
)


_CHANNELCONFIG = _descriptor.Descriptor(
  name='ChannelConfig',
  full_name='xen.ChannelConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channelMapping', full_name='xen.ChannelConfig.channelMapping', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=175,
)


_CHANNELMAPPING = _descriptor.Descriptor(
  name='ChannelMapping',
  full_name='xen.ChannelMapping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='midiChannel', full_name='xen.ChannelMapping.midiChannel', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cvChannelFrom', full_name='xen.ChannelMapping.cvChannelFrom', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cvChannelTo', full_name='xen.ChannelMapping.cvChannelTo', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=177,
  serialized_end=258,
)


_SCALE = _descriptor.Descriptor(
  name='Scale',
  full_name='xen.Scale',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cents', full_name='xen.Scale.cents', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=260,
  serialized_end=282,
)

_CONFIGWRAPPER.fields_by_name['channelConfig'].message_type = _CHANNELCONFIG
_CONFIGWRAPPER.fields_by_name['scale'].message_type = _SCALE
_CHANNELCONFIG.fields_by_name['channelMapping'].message_type = _CHANNELMAPPING
DESCRIPTOR.message_types_by_name['ConfigWrapper'] = _CONFIGWRAPPER
DESCRIPTOR.message_types_by_name['ChannelConfig'] = _CHANNELCONFIG
DESCRIPTOR.message_types_by_name['ChannelMapping'] = _CHANNELMAPPING
DESCRIPTOR.message_types_by_name['Scale'] = _SCALE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConfigWrapper = _reflection.GeneratedProtocolMessageType('ConfigWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGWRAPPER,
  '__module__' : 'ConfigMessage_pb2'
  # @@protoc_insertion_point(class_scope:xen.ConfigWrapper)
  })
_sym_db.RegisterMessage(ConfigWrapper)

ChannelConfig = _reflection.GeneratedProtocolMessageType('ChannelConfig', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELCONFIG,
  '__module__' : 'ConfigMessage_pb2'
  # @@protoc_insertion_point(class_scope:xen.ChannelConfig)
  })
_sym_db.RegisterMessage(ChannelConfig)

ChannelMapping = _reflection.GeneratedProtocolMessageType('ChannelMapping', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELMAPPING,
  '__module__' : 'ConfigMessage_pb2'
  # @@protoc_insertion_point(class_scope:xen.ChannelMapping)
  })
_sym_db.RegisterMessage(ChannelMapping)

Scale = _reflection.GeneratedProtocolMessageType('Scale', (_message.Message,), {
  'DESCRIPTOR' : _SCALE,
  '__module__' : 'ConfigMessage_pb2'
  # @@protoc_insertion_point(class_scope:xen.Scale)
  })
_sym_db.RegisterMessage(Scale)


# @@protoc_insertion_point(module_scope)
