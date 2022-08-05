from pathlib import Path
from typing import List

def get_input(caller: str, path = './input.txt') -> str:
    '''Returns the string contained in the file relative to the given caller path. ./index.txt is used by default'''

    input_path = Path(caller).parent.joinpath(path).resolve()

    with open(input_path) as input:
        return input.read()
