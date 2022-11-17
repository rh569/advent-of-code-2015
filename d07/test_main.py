import pytest

from d07.lib import part_one
from utils.input import get_lines

@pytest.mark.parametrize('target,value', [
    ('d', 72),
    ('e', 507),
    ('f', 492),
    ('g', 114),
    ('h', 65412),
    ('i', 65079),
    ('x', 123),
    ('y', 456)
])
def test_part_one(target, value):
    input = get_lines(__file__, "./testInput.txt")
    
    assert part_one(input, target) == value
