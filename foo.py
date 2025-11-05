from random import randint


class Foo:
    def __init__(self):
        self.x = str(randint(1, 1_000))

    def __repr__(self):
        return self.x
