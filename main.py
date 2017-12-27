import math


class MainFunctions(object):
    def add(self, *args):
        result = sum(args)
        return result

    def subtract(self, *args):
        for i in range(1, len(args)):
            if i == 1:
                result = args[i-1] - args[i]
            else:
                result = result - args[i]
        return result

    def multiply(self):
        pass

    def divide(self):
        pass

    def modulus(self):
        pass

    def squareRoot(self):
        pass

    def square(self):
        pass

    def cube(self):
        pass

    def inverse(self):
        pass
