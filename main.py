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

    def multiply(self, *args):
        result = 1
        for i in args:
            result = result * i
        return result

    def divide(self, *args):
        for i in range(1, len(args)):
            if args[i] == 0:
                return "Cannot divide by 0"
            elif i == 1:
                result = args[i-1] / args[i]
            else:
                result = result / args[i]
        return round(result, 12)

    def modulus(self):
        pass

    def squareRoot(self, number=None):
        if number is None:
            return "Invalid Input"
        elif number < 0:
            return "Invalid Input"
        else:
            result = math.sqrt(number)
            return result

    def powerOfTwo(self, number=None):
        if number is None:
            return "Invalid Input"
        else:
            return math.pow(number, 2)

    def cube(self, number=None):
        if number is None:
            return "Invalid Input"
        else:
            return math.pow(number, 3)

    def inverse(self, number=None):
        if number is None or number == 0:
            return "Invalid Input"
        else:
            return round(1/number, 12)
