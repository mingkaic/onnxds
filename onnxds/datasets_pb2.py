# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: onnxds/datasets.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from onnx import onnx_pb2 as onnx_dot_onnx__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='onnxds/datasets.proto',
  package='onnx_dataset',
  syntax='proto3',
  serialized_options=_b('H\003'),
  serialized_pb=_b('\n\x15onnxds/datasets.proto\x12\x0connx_dataset\x1a\x0fonnx/onnx.proto\"f\n\x0c\x44\x61tasetEntry\x12#\n\x06tensor\x18\x01 \x01(\x0b\x32\x11.onnx.TensorProtoH\x00\x12(\n\x07\x64\x61taset\x18\x02 \x01(\x0b\x32\x15.onnx_dataset.DatasetH\x00\x42\x07\n\x05\x65ntry\"\x8a\x01\n\nDatasetMap\x12\x32\n\x05\x64icts\x18\x01 \x03(\x0b\x32#.onnx_dataset.DatasetMap.DictsEntry\x1aH\n\nDictsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.onnx_dataset.DatasetEntry:\x02\x38\x01\"m\n\x0b\x44\x61tasetIter\x12+\n\x05\x65ntry\x18\x01 \x01(\x0b\x32\x1a.onnx_dataset.DatasetEntryH\x00\x12)\n\x05\x64icts\x18\x02 \x01(\x0b\x32\x18.onnx_dataset.DatasetMapH\x00\x42\x06\n\x04iter\"3\n\x07\x44\x61taset\x12(\n\x05iters\x18\x01 \x03(\x0b\x32\x19.onnx_dataset.DatasetIterB\x02H\x03\x62\x06proto3')
  ,
  dependencies=[onnx_dot_onnx__pb2.DESCRIPTOR,])




_DATASETENTRY = _descriptor.Descriptor(
  name='DatasetEntry',
  full_name='onnx_dataset.DatasetEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensor', full_name='onnx_dataset.DatasetEntry.tensor', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataset', full_name='onnx_dataset.DatasetEntry.dataset', index=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='entry', full_name='onnx_dataset.DatasetEntry.entry',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=56,
  serialized_end=158,
)


_DATASETMAP_DICTSENTRY = _descriptor.Descriptor(
  name='DictsEntry',
  full_name='onnx_dataset.DatasetMap.DictsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='onnx_dataset.DatasetMap.DictsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='onnx_dataset.DatasetMap.DictsEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=299,
)

_DATASETMAP = _descriptor.Descriptor(
  name='DatasetMap',
  full_name='onnx_dataset.DatasetMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dicts', full_name='onnx_dataset.DatasetMap.dicts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DATASETMAP_DICTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=299,
)


_DATASETITER = _descriptor.Descriptor(
  name='DatasetIter',
  full_name='onnx_dataset.DatasetIter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entry', full_name='onnx_dataset.DatasetIter.entry', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dicts', full_name='onnx_dataset.DatasetIter.dicts', index=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='iter', full_name='onnx_dataset.DatasetIter.iter',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=301,
  serialized_end=410,
)


_DATASET = _descriptor.Descriptor(
  name='Dataset',
  full_name='onnx_dataset.Dataset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iters', full_name='onnx_dataset.Dataset.iters', index=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=412,
  serialized_end=463,
)

_DATASETENTRY.fields_by_name['tensor'].message_type = onnx_dot_onnx__pb2._TENSORPROTO
_DATASETENTRY.fields_by_name['dataset'].message_type = _DATASET
_DATASETENTRY.oneofs_by_name['entry'].fields.append(
  _DATASETENTRY.fields_by_name['tensor'])
_DATASETENTRY.fields_by_name['tensor'].containing_oneof = _DATASETENTRY.oneofs_by_name['entry']
_DATASETENTRY.oneofs_by_name['entry'].fields.append(
  _DATASETENTRY.fields_by_name['dataset'])
_DATASETENTRY.fields_by_name['dataset'].containing_oneof = _DATASETENTRY.oneofs_by_name['entry']
_DATASETMAP_DICTSENTRY.fields_by_name['value'].message_type = _DATASETENTRY
_DATASETMAP_DICTSENTRY.containing_type = _DATASETMAP
_DATASETMAP.fields_by_name['dicts'].message_type = _DATASETMAP_DICTSENTRY
_DATASETITER.fields_by_name['entry'].message_type = _DATASETENTRY
_DATASETITER.fields_by_name['dicts'].message_type = _DATASETMAP
_DATASETITER.oneofs_by_name['iter'].fields.append(
  _DATASETITER.fields_by_name['entry'])
_DATASETITER.fields_by_name['entry'].containing_oneof = _DATASETITER.oneofs_by_name['iter']
_DATASETITER.oneofs_by_name['iter'].fields.append(
  _DATASETITER.fields_by_name['dicts'])
_DATASETITER.fields_by_name['dicts'].containing_oneof = _DATASETITER.oneofs_by_name['iter']
_DATASET.fields_by_name['iters'].message_type = _DATASETITER
DESCRIPTOR.message_types_by_name['DatasetEntry'] = _DATASETENTRY
DESCRIPTOR.message_types_by_name['DatasetMap'] = _DATASETMAP
DESCRIPTOR.message_types_by_name['DatasetIter'] = _DATASETITER
DESCRIPTOR.message_types_by_name['Dataset'] = _DATASET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DatasetEntry = _reflection.GeneratedProtocolMessageType('DatasetEntry', (_message.Message,), {
  'DESCRIPTOR' : _DATASETENTRY,
  '__module__' : 'onnxds.datasets_pb2'
  # @@protoc_insertion_point(class_scope:onnx_dataset.DatasetEntry)
  })
_sym_db.RegisterMessage(DatasetEntry)

DatasetMap = _reflection.GeneratedProtocolMessageType('DatasetMap', (_message.Message,), {

  'DictsEntry' : _reflection.GeneratedProtocolMessageType('DictsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATASETMAP_DICTSENTRY,
    '__module__' : 'onnxds.datasets_pb2'
    # @@protoc_insertion_point(class_scope:onnx_dataset.DatasetMap.DictsEntry)
    })
  ,
  'DESCRIPTOR' : _DATASETMAP,
  '__module__' : 'onnxds.datasets_pb2'
  # @@protoc_insertion_point(class_scope:onnx_dataset.DatasetMap)
  })
_sym_db.RegisterMessage(DatasetMap)
_sym_db.RegisterMessage(DatasetMap.DictsEntry)

DatasetIter = _reflection.GeneratedProtocolMessageType('DatasetIter', (_message.Message,), {
  'DESCRIPTOR' : _DATASETITER,
  '__module__' : 'onnxds.datasets_pb2'
  # @@protoc_insertion_point(class_scope:onnx_dataset.DatasetIter)
  })
_sym_db.RegisterMessage(DatasetIter)

Dataset = _reflection.GeneratedProtocolMessageType('Dataset', (_message.Message,), {
  'DESCRIPTOR' : _DATASET,
  '__module__' : 'onnxds.datasets_pb2'
  # @@protoc_insertion_point(class_scope:onnx_dataset.Dataset)
  })
_sym_db.RegisterMessage(Dataset)


DESCRIPTOR._options = None
_DATASETMAP_DICTSENTRY._options = None
# @@protoc_insertion_point(module_scope)
