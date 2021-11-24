#!/usr/bin/env python3

from utils import get_input

input = get_input(2020, 5)

def get_id(boarding_pass: bytes) -> int:
  binary_rep = boarding_pass \
    .replace(b"F", b"0") \
    .replace(b"B", b"1") \
    .replace(b"R", b"1") \
    .replace(b"L", b"0")
  return int(binary_rep[:7], 2) * 8 + int(binary_rep[7:], 2) 

seat_ids = [get_id(item) for item in input.splitlines()]

print(max(seat_ids))

seats_with_empty_front = [item - 1 for item in seat_ids if item - 1 not in seat_ids]
seats_with_empty_back = [item + 1 for item in seat_ids if item + 1 not in seat_ids]
print(list(set(seats_with_empty_front).intersection(seats_with_empty_back))[0])
