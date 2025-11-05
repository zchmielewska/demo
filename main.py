import pickle
from foo import Foo


def run():
    foos = []
    for i in range(100_000):
        foo = Foo()
        foos.append(foo)

    with open("./app/data/foos.pkl", "wb") as f:
        pickle.dump(foos, f)


if __name__ == '__main__':
    run()
