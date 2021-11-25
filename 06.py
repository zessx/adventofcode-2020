#!/usr/bin/env python3

from utils import get_input
from functools import reduce

input = get_input(2020, 6)

groups_inc = []
groups_exc = []
current_inc = []
current_exc = []
for line in input.splitlines():
  if line == b"":
    groups_inc.append(current_inc)
    groups_exc.append(reduce(lambda a, b: list(set(a).intersection(b)), current_exc))
    current_inc = []
    current_exc = []
  else:
    current_inc.extend(list(line))
    current_exc.append(list(line))
groups_inc.append(current_inc)
groups_exc.append(reduce(lambda a, b: list(set(a).intersection(b)), current_exc))

print(sum([len(set(group)) for group in groups_inc]))
print(sum([len(set(group)) for group in groups_exc]))
