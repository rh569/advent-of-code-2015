from typing import Dict, List, Optional, Union
from utils.input import get_lines

Value = Union[str, int]

class Wire:
    id: Optional[str] = None
    signal: Optional[int] = None

    def __init__(self, id_or_signal: str):
        if id_or_signal.isdigit():
            self.signal = int(id_or_signal)
        else:
            self.id = id_or_signal


class Gate:
    output_wire: Wire
    # NOT, OR, AND, LSHIFT, RSHIFT, SOURCE
    op: str
    input_one: Wire
    input_two: Optional[Wire] = None
    shift_amount: Optional[int] = None

    def __init__(self, line: str):
        [ins, out] = line.split(' -> ')

        self.output_wire = Wire(out.strip())

        input_parts = ins.split(' ')
        if (len(input_parts) == 1):
            # SOURCE
            self.op = 'SOURCE'
            self.input_one = Wire(input_parts[0])
        elif (len(input_parts) == 2):
            # NOT
            self.op = 'NOT'
            self.input_one = Wire(input_parts[1])
        elif (len(input_parts) == 3):
            # AND, OR, LSHIFT, RSHIFT
            self.op = input_parts[1]
            self.input_one = Wire(input_parts[0]) 

            if (self.op == 'AND' or self.op == 'OR'):
                self.input_two = Wire(input_parts[2])
            elif (self.op == 'LSHIFT' or self.op == 'RSHIFT'):
                self.shift_amount = int(input_parts[2])
            else:
                raise RuntimeError(f'unrecognised op: {self.op}')
        else:
            raise RuntimeError(f'unexecpeted number of input_parts: {input_parts}')


def make_gate_map(gates: List[Gate]) -> Dict[str, Gate]:
    gates_by_output_id: Dict[str, Gate] = {}

    for g in gates:
        if g.output_wire.id is None:
            raise RuntimeError('anonymous output wire found')
        else:
            gates_by_output_id[g.output_wire.id] = g

    return gates_by_output_id


def process_gate(g: Gate, gates_by_output_id: Dict[str, Gate]) -> None:
    # Handle case where wire signal is already known
    if g.output_wire.signal is not None:
        return

    # Copy input signals from map if known
    if g.input_one.signal is None and g.input_one.id is not None:
        if gates_by_output_id[g.input_one.id].output_wire.signal is not None:
            g.input_one.signal = gates_by_output_id[g.input_one.id].output_wire.signal
    if g.input_two is not None and g.input_two.signal is None and g.input_two.id is not None:
        if gates_by_output_id[g.input_two.id].output_wire.signal is not None:
            g.input_two.signal = gates_by_output_id[g.input_two.id].output_wire.signal

    if g.op == 'SOURCE':
        if g.input_one.signal is not None:
            g.output_wire.signal = g.input_one.signal
    
    if g.op == 'NOT':
        if g.input_one.signal is not None:
            inverse = ~g.input_one.signal

            if inverse < 0:
                # handle two's complement int represenatation
                inverse += 2**16

            g.output_wire.signal = inverse

    if g.op == 'AND':
        if g.input_two is None:
            raise RuntimeError(f'No second input for {g.output_wire.id}')

        if g.input_one.signal is not None and g.input_two.signal is not None:
            g.output_wire.signal = g.input_one.signal & g.input_two.signal
    
    if g.op == 'OR':
        if g.input_two is None:
            raise RuntimeError(f'No second input for {g.output_wire.id}')

        if g.input_one.signal is not None and g.input_two.signal is not None:
            g.output_wire.signal = g.input_one.signal | g.input_two.signal

    if g.op == 'LSHIFT':
        if g.shift_amount is None:
            raise RuntimeError(f'No shift amount for {g.output_wire.id}')

        if g.input_one.signal is not None:
            g.output_wire.signal = g.input_one.signal << g.shift_amount
    
    if g.op == 'RSHIFT':
        if g.shift_amount is None:
            raise RuntimeError(f'No shift amount for {g.output_wire.id}')

        if g.input_one.signal is not None:
            g.output_wire.signal = g.input_one.signal >> g.shift_amount


def run_all_gates(gates: List[Gate], gates_by_output_id: Dict[str, Gate], target: str, pass_limit: int) -> int:
    for _ in range(pass_limit):
        for g in gates:
            process_gate(g, gates_by_output_id)

            if g.output_wire.id == target and g.output_wire.signal is not None:
                return g.output_wire.signal

    raise RuntimeError(f'No solution after {pass_limit} passes')


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
