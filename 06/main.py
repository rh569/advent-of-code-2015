from enum import Enum
from typing import List
from utils.geometry import Vec2
from utils.input import get_lines

class InstructionType(Enum):
    ON = 0
    OFF = 1
    TOGGLE = 2

class Instruction:
    instruction_type: InstructionType

    def __init__(self, line: str):
        [ins, frm, _, to] = line.replace(' o', 'o').split(' ')

        self.instruction_type = self.get_type_from_int(ins)
        self.apply_from = Vec2.from_string(frm)
        self.apply_to = Vec2.from_string(to)

    def get_type_from_int(self, typ: str) -> InstructionType:
        if (typ == 'turnon'):
            return InstructionType.ON
        elif (typ == 'turnoff'):
            return InstructionType.OFF
        elif (typ == 'toggle'):
            return InstructionType.TOGGLE
        else:
            raise

def part_one(input: List[str]):
    return lightshow(input, 1)

def part_two(input: List[str]):
    return lightshow(input, 2)

def lightshow(input: List[str], mode: int):
    instructions = parse_instructions(input)
    lights = make_lights(1000)

    for i in instructions:
        apply_instruction(lights, i, mode)

    return count_lights(lights)

def make_lights(size):
    lights = []

    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        lights.append(row)

    return lights

def parse_instructions(input: List[str]):
    ins: List[Instruction] = []

    for l in input:
        ins.append(Instruction(l))
    
    return ins

def apply_instruction(lights: List[List[int]], ins: Instruction, mode: int):
    for i in range(ins.apply_from.x, ins.apply_to.x + 1):
        for j in range(ins.apply_from.y, ins.apply_to.y + 1):
            lights[i][j] = get_next_state(lights[i][j], ins.instruction_type, mode)

def get_next_state(light: int, typ: InstructionType, mode: int):
    if typ == InstructionType.ON:
        return 1 if mode == 1 else light + 1
    elif typ == InstructionType.OFF:
        return 0 if mode == 1 else max(0, light - 1)
    else:
        if mode == 1:
            return 1 if light == 0 else 0
        else:
            return light + 2

def count_lights(lights: List[List[int]]) -> int:
    count = 0

    for i in lights:
        for j in i:
            count += j

    return count

print(f'Part 1: {part_one(get_lines(__file__))}')
print(f'Part 2: {part_two(get_lines(__file__))}')
