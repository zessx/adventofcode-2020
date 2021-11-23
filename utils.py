#!/usr/bin/env python3

import os
from typing import Any, Mapping
import requests
from dotenv import load_dotenv

load_dotenv()

def get_cookies() -> Mapping:
  return {"session": os.environ["AOC_SESSION_ID"]}

def get_input(year: int, day: int) -> str:
  request = requests.get(f"https://adventofcode.com/{str(year)}/day/{str(day)}/input", 
    cookies = get_cookies())
  return request.content

def post_answer(year: int, day: int, level: int, answer: Any) -> str:
  request = requests.post(f"https://adventofcode.com/{str(year)}/day/{str(day)}/answer", 
    cookies = get_cookies(),
    params = {"level": level, "answer": answer})
  return request.content
