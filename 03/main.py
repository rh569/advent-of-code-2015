from enum import Enum

from utils.input import get_input
from utils.geometry import Vec2

class Dir(Enum):
    UP = '^'
    RIGHT = '>'
    DOWN ='v'
    LEFT = '<'

def countDelivery(pos: Vec2, deliveries):
    key = pos.to_string()
    val = deliveries.get(key)

    if val == None:
        deliveries[key] = 1
    else:
        deliveries[key] += 1

def updatePosition(dir: str, pos: Vec2):
    if Dir.UP.value == dir:
        pos.y +=1
    elif Dir.RIGHT.value == dir:
        pos.x +=1
    elif Dir.DOWN.value == dir:
        pos.y -=1
    elif Dir.LEFT.value == dir:
        pos.x -=1

def part_one(input: str) -> int:
    instructions = list(input)
    deliveries = {}

    pos = Vec2(0, 0)
    countDelivery(pos, deliveries)

    for d in instructions:
        updatePosition(d, pos)        
        countDelivery(pos, deliveries)
    
    return len(deliveries)

def part_two(input: str) -> int:
    instructions = list(input)
    deliveries = {}

    sPos = Vec2(0, 0)
    countDelivery(sPos, deliveries)
    rPos = Vec2(0, 0)
    countDelivery(rPos, deliveries)

    turn = 0

    for d in instructions:
        if turn % 2 == 0:
            updatePosition(d, sPos)
            countDelivery(sPos, deliveries)
        else:
            updatePosition(d, rPos)
            countDelivery(rPos, deliveries)
        
        turn += 1

    return len(deliveries)



print(f'Part 1: {part_one(get_input(__file__))}')
print(f'Part 2: {part_two(get_input(__file__))}')