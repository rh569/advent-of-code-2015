from hashlib import md5

INPUT = 'ckczppom'

def part_one(start: int = 0, leading: str = '00000'):
    salt = start

    hash = ''

    while not hash.startswith(leading):
        salt += 1
        bytes = f'{INPUT}{salt}'.encode('utf-8')
        hash = md5(bytes).hexdigest()

    return salt

def part_two():
    return part_one(117946, '000000')

print(f'Part 1: {part_one()}')
print(f'Part 2: {part_two()}')
