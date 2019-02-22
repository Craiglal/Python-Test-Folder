class Book:
    def __init__(self, author, name, year, genre, reviews=[]):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre
        self.reviews = reviews

    def __repr__(self):
        return f"Book({self.author}, {self.name}, {self.year}, {self.genre})"

    def __str__(self):
        book = f"""
        Author: {self.author}
        Book: {self.name}
        Year: {self.year}
        Genre: {self.genre}
        """
        reviews = ''.join(map(str, self.reviews)) or '\n        No comments.\n'
        return book + reviews

    def __eq__(self, other):
        return self.author == other.author and self.name == other.name and self.year == other.year \
               and self.genre == other.genre


class BookReview:
    def __init__(self, review, stars):
        self.review = review
        self.stars = stars

    def __repr__(self):
        return f"Book({self.review}, {self.stars})"

    def __str__(self):
        return f"""
        Review: {self.review}
        {self.stars} stars.
        """


def main():
    book_one = Book("Alex Asleep", "Kill", "1992", "Action")
    book_two = Book("Alexa Finder", "Auto", "1982", "Action")
    book_three = Book("John Elevar", "The goal", "2001", "Fantasy")

    book_one.reviews = [BookReview("Nice Book!!!", 5),
                        BookReview("Perfect for children!", 4)]

    print(book_one)
    print(book_two)
    print(book_three)


if __name__ == '__main__':
    main()
