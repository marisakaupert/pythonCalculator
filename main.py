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

    def squareRoot(self):
        pass

    def square(self):
        pass

    def cube(self):
        pass

    def inverse(self):
        pass
