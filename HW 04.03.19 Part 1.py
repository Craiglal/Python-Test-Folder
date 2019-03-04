def avr(*args):
    return sum(args) / len(args)


def main():
    print(avr(2, 10))
    print(avr(*range(1, 10)))


if __name__ == "__main__":
    main()

