def myfun():
    print("Hello, World!")


class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")


if __name__ == "__main__":
    myfun()
    obj = MyClass(10)
    obj.display()
