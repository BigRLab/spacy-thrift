#!/usr/bin/env python
#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:utf8strings
#

import sys
import pprint
try:
  from urllib.parse import urlparse
except ImportError:
  from urlparse import urlparse
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift.transport import TSSLSocket
from thrift.transport import THttpClient
from thrift.protocol import TBinaryProtocol

from spacyThrift import SpacyThrift
from spacyThrift.ttypes import *

if len(sys.argv) <= 1 or sys.argv[1] == '--help':
  print('')
  print('Usage: ' + sys.argv[0] + ' [-h host[:port]] [-u url] [-f[ramed]] [-s[sl]] function [arg1 [arg2...]]')
  print('')
  print('Functions:')
  print('   tag(string sentence)')
  print('')
  sys.exit(0)

pp = pprint.PrettyPrinter(indent = 2)
host = 'localhost'
port = 9090
uri = ''
framed = False
ssl = False
http = False
argi = 1

if sys.argv[argi] == '-h':
  parts = sys.argv[argi+1].split(':')
  host = parts[0]
  if len(parts) > 1:
    port = int(parts[1])
  argi += 2

if sys.argv[argi] == '-u':
  url = urlparse(sys.argv[argi+1])
  parts = url[1].split(':')
  host = parts[0]
  if len(parts) > 1:
    port = int(parts[1])
  else:
    port = 80
  uri = url[2]
  if url[4]:
    uri += '?%s' % url[4]
  http = True
  argi += 2

if sys.argv[argi] == '-f' or sys.argv[argi] == '-framed':
  framed = True
  argi += 1

if sys.argv[argi] == '-s' or sys.argv[argi] == '-ssl':
  ssl = True
  argi += 1

cmd = sys.argv[argi]
args = sys.argv[argi+1:]

if http:
  transport = THttpClient.THttpClient(host, port, uri)
else:
  socket = TSSLSocket.TSSLSocket(host, port, validate=False) if ssl else TSocket.TSocket(host, port)
  if framed:
    transport = TTransport.TFramedTransport(socket)
  else:
    transport = TTransport.TBufferedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = SpacyThrift.Client(protocol)
transport.open()

if cmd == 'tag':
  if len(args) != 1:
    print('tag requires 1 args')
    sys.exit(1)
  pp.pprint(client.tag(args[0],))

else:
  print('Unrecognized method %s' % cmd)
  sys.exit(1)

transport.close()
