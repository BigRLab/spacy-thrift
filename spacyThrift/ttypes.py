#
# Autogenerated by Thrift Compiler (0.11.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class Token(object):
    """
    Attributes:
     - text
     - tag
     - lemma
     - entity
    """


    def __init__(self, text=None, tag=None, lemma=None, entity=None,):
        self.text = text
        self.tag = tag
        self.lemma = lemma
        self.entity = entity

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.text = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.tag = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.lemma = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.entity = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Token')
        if self.text is not None:
            oprot.writeFieldBegin('text', TType.STRING, 1)
            oprot.writeString(self.text.encode('utf-8') if sys.version_info[0] == 2 else self.text)
            oprot.writeFieldEnd()
        if self.tag is not None:
            oprot.writeFieldBegin('tag', TType.STRING, 2)
            oprot.writeString(self.tag.encode('utf-8') if sys.version_info[0] == 2 else self.tag)
            oprot.writeFieldEnd()
        if self.lemma is not None:
            oprot.writeFieldBegin('lemma', TType.STRING, 3)
            oprot.writeString(self.lemma.encode('utf-8') if sys.version_info[0] == 2 else self.lemma)
            oprot.writeFieldEnd()
        if self.entity is not None:
            oprot.writeFieldBegin('entity', TType.STRING, 4)
            oprot.writeString(self.entity.encode('utf-8') if sys.version_info[0] == 2 else self.entity)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Token)
Token.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'text', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'tag', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'lemma', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'entity', 'UTF8', None, ),  # 4
)
fix_spec(all_structs)
del all_structs
