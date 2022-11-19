from typing import List

from days.day_07.lib import Gate, make_gate_map, run_all_gates
from utils.input import get_lines

def part_one(input: List[str], target: str):
    gates = list(map(Gate, input))
    gates_by_output_id = make_gate_map(gates)

    return run_all_gates(gates, gates_by_output_id, target, 1000)


def part_two(input: List[str], target: str):
    gates = list(map(Gate, input))
    gates_by_output_id = make_gate_map(gates)

    # Set signal for 'b' to that of 'a' from part one
    gates_by_output_id["b"].input_one.signal = part_one(get_lines(__file__), "a")

    return run_all_gates(gates, gates_by_output_id, target, 1000)


def run():
    print(f'Part 1: {part_one(get_lines(__file__), "a")}')
    print(f'Part 2: {part_two(get_lines(__file__), "a")}')
