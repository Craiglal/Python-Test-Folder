def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Error: division by zero!")


def power(num1, pwr):
    try:
        return num1 ** pwr
    except ZeroDivisionError:
        print("Error: You can't have a negative power to 0!")


def inp():
    num1 = float(input("Enter the first number: "))
    op = input("Enter operation(+, -, *, /, ^): ")
    if op == '+' or op == '-' or op == '*' or op == '/':
        num2 = float(input("Enter the second number: "))
        if op == '+':
            print(" = ", add(num1, num2))
        elif op == '-':
            print(" = ", sub(num1, num2))
        elif op == '*':
            print(" = ", mul(num1, num2))
        else:
            print(" = ", div(num1, num2))
    elif op == '^':
        pwr = int(input("Enter the power(^): "))
        print(" = ", power(num1, pwr))
    else:
        print("Wrong operation!")


def main():
    run = True
    while run:
        inp()


if __name__ == "__main__":
    main()
