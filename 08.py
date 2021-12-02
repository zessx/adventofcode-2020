#!/usr/bin/env python3

from typing import Union
from utils import get_input
from copy import deepcopy

input = get_input(2020, 8)
items = list(map(lambda x: {"ops": x.split()[0], "arg": int(x.split()[1])}, input.splitlines()))

def run(operations: list, calculate: bool = False) -> Union[int, bool]:
  ops_executed = []
  accumulator = 0
  i = 0

  while i not in ops_executed and i < len(items):
    ops_executed.append(i)
    jmp = 1
    if operations[i]["ops"] == b"acc" and calculate:
      accumulator += operations[i]["arg"]
    if operations[i]["ops"] == b"jmp":
      jmp = operations[i]["arg"]
    i += jmp

  if calculate:
    return accumulator

  return i == len(operations)

print(run(items, True))

for k, i in enumerate(items):
  if i["ops"] == b"jmp":
    variant = deepcopy(items)
    variant[k]["ops"] = b"nop"
    if run(variant):
      print(run(variant, True))
  elif i["ops"] == b"nop":
    variant = deepcopy(items)
    variant[k]["ops"] = b"jmp"
    if run(variant):
      print(run(variant, True))