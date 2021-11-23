#!/usr/bin/env python3

from utils import get_input

input = get_input(2020, 1)

items = list(map(lambda x: int(x), input.splitlines()))

half = 2020 / 2
half_items = [item for item in items if item <= half]
matching_items = [item for item in items if 2020 - item in half_items]
answer_part1 = matching_items[0] * (2020 - matching_items[0])

print(answer_part1)

third = 2020 / 3
third_items = [item for item in items if item <= third]
for third_item in third_items:
  half = (2020 - third_item) / 2 
  half_items = [item for item in items if item <= half and item != third_item]
  matching_items = [item for item in items if 2020 - third_item - item in items]
  if len(matching_items) > 0:
    answer_part2 = matching_items[0] * third_item * (2020 - matching_items[0] - third_item)

print(answer_part2)

