from datetime import date

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_string(cls, str: str):
        parts = str.split(',')

        return (int(parts[0]), int(parts[1]))

    def to_string(self):
        return f'{self.x},{self.y}'

