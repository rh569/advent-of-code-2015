
from typing import List
from utils.input import get_lines

def part_one(input: List[str]):
    count = 0

    for l in input:
        if is_nice_string(l):
            count += 1
    
    return count

def is_nice_string(s: str):
    last_char = None

    n_vowels_met = 0
    any_double_met = False
    no_exclusions_met = True

    for c in list(s):
        if c in ['a', 'e', 'i', 'o', 'u']:
            n_vowels_met += 1

        if c == last_char:
            any_double_met = True

        if f'{last_char}{c}' in ['ab', 'cd', 'pq', 'xy']:
            no_exclusions_met = False

        last_char = c

    return n_vowels_met > 2 and any_double_met and no_exclusions_met

def part_two(input: List[str]):
    count = 0

    for l in input:
        if is_new_nice_string(l):
            count += 1
    
    return count

def is_new_nice_string(s: str):
    last_pair = None

    unique_pairs_by_initial_index = {}

    # xyxy but not aaa
    has_repeated_pair = False
    # xyx or aaa
    has_repeated_letter = False

    # Able to use just one loop by using a moving frame of pairs,
    # tracking the last pair, and tracking when each unique pair
    # was first seen in the string
    for i in range(len(s) - 1):
        pair = s[i] + s [i+1]

        if unique_pairs_by_initial_index.get(pair) == None:
            unique_pairs_by_initial_index[pair] = i
        elif i - unique_pairs_by_initial_index[pair] > 1:
            has_repeated_pair = True

        if last_pair != None:
            if last_pair[0] == pair[1]:
                has_repeated_letter = True

        last_pair = pair

    return has_repeated_pair and has_repeated_letter

print(f'Part 1: {part_one(get_lines(__file__))}')
print(f'Part 2: {part_two(get_lines(__file__))}')
