def add_function(first, second):
    return first + second

def mul_function(first, second):
    return first * second

def sub_function(first, second):
    return first - second

def div_function(first, second):
    return first / second


class Calculator:

    def setdate(self, first, second):
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

   # c = Calculator()
   # c.setdate(1,4)

    print(add_function(8,2))
    print(mul_function(8,2))
    print(sub_function(8,2))
    print(div_function(8,2))




