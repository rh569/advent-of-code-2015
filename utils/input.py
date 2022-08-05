from pathlib import Path
from typing import List

def get_input(caller: str, path = './input.txt') -> str:
    '''Returns the string contained in the file relative to the given caller path. ./index.txt is used by default'''

    input_path = Path(caller).parent.joinpath(path).resolve()

    with open(input_path) as input:
        return input.read()

def get_lines(caller: str, path = './input.txt') -> List[str]:
    '''Returns the non-empty lines contained in the file as a List relative to the given caller path. ./index.txt is used by default'''

    input_path = Path(caller).parent.joinpath(path).resolve()

    with open(input_path) as input:
        return list(filter(not_empty, input.readlines()))

def not_empty(s: str) -> bool:
    return len(s.strip()) > 0
