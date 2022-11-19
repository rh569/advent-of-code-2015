import importlib
import os
import sys

def run_day(d: str):
    day_module = importlib.import_module(f'days.{d}.main')

    try:
        print(f'Running {d}...')
        day_module.run()
        print()
    except:
        print(f'Run method not defined for day "{d}"')


def get_all_days():
    days = next(os.walk('./days/'))[1]
    days.sort()

    return days


def run_all_days():
    for d in get_all_days():
        run_day(d)

# --- 

if len(sys.argv) < 2:
    print('No day given to run\n')
    print('Examples:')
    print('    python run.py 01')
    print('    python run.py day_01')
    print('    python run.py all')

    exit(1)

input = sys.argv[1]

if input == 'all':
    print('Running all days...\n')
    run_all_days()
    print('\nComplete.\n')

    exit(0)


if len(input) == 1:
    input = f'0{input}'

if not input.startswith('day_'):
    input = f'day_{input}'

days = get_all_days()

if not input in days:
    print(f'Given day "{input}" not found.\n')
    print(f'Available days:')

    for d in days:
        print(f'    {d}')

    exit(1)

run_day(input)
