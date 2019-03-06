class MyException(Exception):
    pass


def f(*args):
    count = 0
    for x in args:
        if x % 2 == 1:
            count = count + 1

    if count % 2 == 1:
        return args
    else:
        raise MyException


def main():
    print(f(1, 2, 3, 4, 5, 6))


if __name__ == "__main__":
    main()
