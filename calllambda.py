class Surprise(Exception):  # ЗАДАЧА 1
    pass


def f(operation):
    if operation == "plus":
        def plus(a, b):
            return a + b

        return plus
    elif operation == "minus":
        def minus(a, b):
            return a - b

        return minus
    else:
        raise Surprise()


try:
    var = f("minus")
    print(var(5, '3'))
except Exception:
    print('Попробуйте ещё раз')

# ЗАДАЧА 2
sample1 = lambda x: x ** 2
print(sample1(11))


def sample2(x):
    return x ** 2


print(sample2(11))


# ЗАДАЧА 3
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


example = Rect(6, 6)
print(example())
