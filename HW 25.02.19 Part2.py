#class GraphicObject(object):
#    def mouse_click(self):


class Square(object):
    def __init__(self, width):
        self.width = width

    def draw(self):
        for i in range(self.width):
            for j in range(self.width):
                if i == 0 or i == self.width:
                    print('*', end='')
                elif 0 < i < self.width:
                    if j == 0 or j == self.width:
                        print('*', end='')
        print()


#class Button(object):

obj = Square(int(input("The width: ")))
obj.draw()