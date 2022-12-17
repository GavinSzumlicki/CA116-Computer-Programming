#!/usr/bin/env python3

import sys
url = sys.argv[1]

x = 0
y = 0
z = 0

tokens = url.split("://")
scheme = tokens[0]
url = tokens[1]

tokens = url.split("#")
if 1 < len(tokens):
  fragment = tokens[1]
  x = 1
url = tokens[0]

tokens = url.split("?")
if 1 < len(tokens):
  query = tokens[1]
  y = 1
url = tokens[0]

tokens = url.split("/")
host_port = tokens[0]

path = "/" + "/".join(tokens[1:])

tokens = host_port.split(":")
host = tokens[0]
if 1 < len(tokens):
  port = tokens[1]
  z = 1


print("scheme:", scheme)
print("host:", host)
if z == 1:
  print("port:", port)
print("path:", path)
if y == 1:
  print("query-string:", query)
if x == 1:
  print("fragment-id:", fragment)
