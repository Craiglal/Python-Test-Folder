def main():
    unnessesery = (" ", ",", ".", "-", "_")
    first_str = input("The first string: ")
    second_str = input("The second string: ")
    tmp = set(first_str.replace(" ", "")) & set(second_str.replace(" ", ""))
    print(" ".join(tmp))

if __name__ == "__main__":
    main()
