#!/usr/bin/env python3

from utils import get_input
import re

input = get_input(2020, 7)

rules = {}
for rule in input.splitlines():
  key = re.match(rb"^(?P<key>\w+\s\w+) bags contain", rule).groupdict()["key"]
  values = re.findall(rb".(?P<amount>\d+) (?P<type>\w+\s\w+) bags?", rule)
  rules[key] = {}
  for amount, type in values:
    rules[key][type] = int(amount)

def bags_can_contains(bag) -> set:
  bags = set([key for key, value in rules.items() if bag in value.keys()])
  for key in bags.copy():
    bags.update(bags_can_contains(key))
  return bags

def bag_contains(bag) -> int:
  return sum([value + value * bag_contains(key) for key, value in rules[bag].items()])

print(len(bags_can_contains(b"shiny gold")))
print(bag_contains(b"shiny gold"))
