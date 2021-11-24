#!/usr/bin/env python3

from utils import get_input
from math import ceil, floor

input = get_input(2020, 3)

def count_trees(shiftr: int, shiftd: int) -> int:
  lines = input.splitlines()
  height = len(lines)
  segment_width = len(lines[0])
  required_width = height * shiftr + 1
  required_segments = ceil(required_width / segment_width)
  lines_extended = list(map(lambda line: line * required_segments, lines))
  return len([1 for i in range(shiftd, height, shiftd) if chr(lines_extended[i][floor(i / shiftd) * shiftr]) == "#"])

print(count_trees(3, 1))

print(
  count_trees(1, 1) *
  count_trees(3, 1) * 
  count_trees(5, 1) *
  count_trees(7, 1) *
  count_trees(1, 2))