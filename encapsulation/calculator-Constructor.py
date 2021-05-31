class Calculator:

    def __init__(self,first,second):
        self.first = first
        self.second = second

    def add(self):
        return c.first + c.second

    def mul(self):
        return c.first * c.second

    def sub(self):
        return c.first - c.second

    def div(self):
        return c.first / c.second


if __name__ == '__main__':
    c = Calculator(1,2)
    print(f'{c.first} + {c.second} = {c.add()}')
    print(f'{c.first} + {c.second} = {c.mul()}')
    print(f'{c.first} + {c.second} = {c.sub()}')
    print(f'{c.first} + {c.second} = {c.mul()}')




