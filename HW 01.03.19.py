import math


class ListObject(object):
    def __init__(self, first, last=None, step=-1):
        if last is None:
            self.start = 0
            self.end = first
        else:
            self.start = first
            self.end = last

        if step == 0:
            raise ValueError('step must not be zero')
        else:
            self.step = step

        length = math.ceil((self.end - self.start) / self.step)
        self.length = length if length >= 0 else 0

        self.elements_returned = 0
        self.current = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.elements_returned >= self.length:
            raise StopIteration

        self.elements_returned += 1

        if self.current is None:
            self.current = self.start
        else:
            self.current += self.step

        return self.current


def main():
    lst = ListObject(10, -11)
    try:
        while True:
            print(next(lst))
    except StopIteration:
        print("End!")


if __name__ == "__main__":
    main()