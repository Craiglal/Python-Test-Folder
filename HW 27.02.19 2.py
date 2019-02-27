class Worker(object):
    def __init__(self, name, surname, depart, year):
        self.name = name
        self.surname = surname
        self.depart = depart
        self.year = year


def main():
    name = input("Name: ")
    surname = input("Surname: ")
    depart = input("Department: ")
    year = input("Year: ")
    id1 = Worker(name, surname, depart, year)

    name = input("Name: ")
    surname = input("Surname: ")
    depart = input("Department: ")
    year = input("Year: ")
    id2 = Worker(name, surname, depart, year)

    name = input("Name: ")
    surname = input("Surname: ")
    depart = input("Department: ")
    year = input("Year: ")
    id3 = Worker(name, surname, depart, year)

    print()

if __name__ == "__main__":
    main()
