import re

from typing import List
from utils.input import get_lines

def part_one(input: List[str]):
    literal_chars = 0
    memory_chars = 0

    for l in input:
        l = l.strip()
        lc = len(l)

        # Remove outer quotes
        l = l[1:-1]

        l = l.replace("\\\"", "\"")
        l = l.replace("\\\\", "\\")
        
        hexcode = re.compile(r"\\x[0-9a-f]{2}")
        l = re.sub(hexcode, "_", l)

        lm = len(l)

        literal_chars += lc
        memory_chars += lm
    
    return literal_chars - memory_chars


def part_two(input: List[str]):
    literal_chars = 0
    escaped_chars = 0

    for l in input:
        l = l.strip()
        lc = len(l)

        l = l.replace("\\", "\\\\")
        l = l.replace("\"", "\\\"")

        l = f'"{l}"'

        le = len(l)

        literal_chars += lc
        escaped_chars += le
    
    return escaped_chars - literal_chars

def run():
    print(f'Part 1: {part_one(get_lines(__file__))}')
    print(f'Part 2: {part_two(get_lines(__file__))}')
