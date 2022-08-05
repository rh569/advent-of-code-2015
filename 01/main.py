from utils.input import get_input

def part_one(input: str) -> int:
    floor = 0

    for c in input:
        if (c == '('):
            floor += 1
        if (c == ')'):
            floor -= 1
    
    return floor

def part_two(input: str) -> int:
    floor = 0

    for i in range(0, len(input)):
        if (input[i] == '('):
            floor += 1
        if (input[i] == ')'):
            floor -= 1

        if floor == -1:
            return i + 1

    raise RuntimeError('did not reach basement (floor -1)')

print(f'Part 1: {part_one(get_input(__file__))}')
print(f'Part 2: {part_two(get_input(__file__))}')
