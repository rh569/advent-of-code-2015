from functools import reduce
from utils.input import get_lines
from typing import List

def part_one(input: List[str]) -> int:
    total_area = 0

    for ln in input:
        l, w, h = list(map(int, ln.split('x')))

        face_areas = [l*w, w*h, l*h]
        face_areas.sort()

        present_area = 3*face_areas[0] + 2*face_areas[1] + 2*face_areas[2]

        total_area += present_area

    return total_area

def part_two(input: List[str]) -> int:
    total_length = 0

    for ln in input:
        l, w, h = list(map(int, ln.split('x')))

        face_perims = [2*l + 2*w, 2*w + 2*h, 2*l + 2*h]
        face_perims.sort()

        present_length = face_perims[0] + l*w*h

        total_length += present_length

    return total_length

print(f'Part 1: {part_one(get_lines(__file__))}')
print(f'Part 2: {part_two(get_lines(__file__))}')
