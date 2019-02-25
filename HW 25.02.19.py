class Editor(object):
    def view_document(self):
        print("You can open it!")

    def edit_document(self):
        print("You can't edit it! You have a free version.")


class ProEditor(Editor):
    def edit_document(self):
        print('You can edit it!')


def main():
    key = input("Your license key: ")

    if key == "12345678":
        user_one = ProEditor()
    else:
        print('Incorrect license key.')
        user_one = Editor()

    user_one.edit_document()
    user_one.view_document()


if __name__ == '__main__':
    main()