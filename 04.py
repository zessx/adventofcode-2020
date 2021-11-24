#!/usr/bin/env python3

from typing import Dict
import re
from utils import get_input

input = get_input(2020, 4)

passports = []
current_passport = {}
for line in input.splitlines():
  if line == b"":
    passports.append(current_passport)
    current_passport = {}
  else:
    for field in line.split():
      key, value = field.split(b":")
      current_passport[key] = value
passports.append(current_passport)

def is_passport_valid_1(passport: Dict) -> bool:
  return len(passport) == 8 or (len(passport) == 7 and b"cid" not in passport)

print(len([p for p in passports if is_passport_valid_1(p)]))

def is_passport_valid_2(passport: Dict) -> bool:
  return (len(passport) == 8 or (len(passport) == 7 and b"cid" not in passport)) and \
    re.match(rb"^\d{4}$", passport[b"byr"]) and 1920 <= int(passport[b"byr"]) <= 2002 and \
    re.match(rb"^\d{4}$", passport[b"iyr"]) and 2010 <= int(passport[b"iyr"]) <= 2020 and \
    re.match(rb"^\d{4}$", passport[b"eyr"]) and 2020 <= int(passport[b"eyr"]) <= 2030 and \
    ( \
      (re.match(rb"^\d+cm$", passport[b"hgt"]) and 150 <= int(passport[b"hgt"][:-2]) <= 193) or \
      (re.match(rb"^\d+in$", passport[b"hgt"]) and 59 <= int(passport[b"hgt"][:-2]) <= 76) \
    ) and \
    re.match(rb"^\#[0-9a-f]{6}$", passport[b"hcl"]) and \
    passport[b"ecl"] in (b"amb", b"blu", b"brn", b"gry", b"grn", b"hzl", b"oth") and \
    re.match(rb"^\d{9}$", passport[b"pid"])

print(len([p for p in passports if is_passport_valid_2(p)]))
