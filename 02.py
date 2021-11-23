#!/usr/bin/env python3

from utils import get_input
import re

input = get_input(2020, 2)

def check_policy_1(line: bytes) -> bool:
  m = re.match(rb"^(?P<min>\d+)-(?P<max>\d+)\s(?P<letter>[a-z]):\s(?P<password>[a-z]+)$", line).groupdict()
  return int(m["min"]) <= m["password"].count(m["letter"]) <= int(m["max"])

print(len([line for line in input.splitlines() if check_policy_1(line)]))

def check_policy_2(line: bytes) -> bool:
  m = re.match(rb"^(?P<i1>\d+)-(?P<i2>\d+)\s(?P<letter>[a-z]):\s(?P<password>[a-z]+)$", line).groupdict()
  return int(str.encode(chr(m["password"][int(m["i1"]) - 1])) == m["letter"]) \
    + int(str.encode(chr(m["password"][int(m["i2"]) - 1])) == m["letter"]) == 1

print(len([line for line in input.splitlines() if check_policy_2(line)]))