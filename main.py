import pickle
from random import randint


class Foo:
    def __init__(self):
        self.x = randint(1, 1_000)

    def __repr__(self):
        return self.x


def run():
    foos = []
    for i in range(100_000):
        foo = Foo()
        foos.append(foo)

    with open("./app/data/foos.pkl", "wb") as f:
        pickle.dump(foos, f)


if __name__ == '__main__':
    run()
