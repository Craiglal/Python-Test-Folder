class GrafObj(object):
    def show(self):
        try:
            self.on_click()
        except AttributeError:
            print(self.__class__.__name__, "can't be clicked!")


class Square(GrafObj):
    def __init__(self, length, text='*  '):
        self.length = length
        self.text = text

    def draw(self):
        for i in range(self.length):
            for j in range(self.length):
                print(self.text, end='')
            print()


class Click(object):
    def on_click(self):
        print(self.__class__.__name__, "is clickable!")


class Button(Square, Click):
    def __init__(self, length, text="*  "):
        super().__init__(length, text)


def main():
    square = Square(5)
    square.draw()
    square.show()

    button = Button(5)
    button.draw()
    button.show()


if __name__ == "__main__":
    main()
