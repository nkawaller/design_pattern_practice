# Checking out examples from this article:
# https://medium.com/better-programming/decorator-pattern-and-python-decorators-b0b573f4c1ce


class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def process(self):
        print("I'm an add process")
        return self.a + self.b


# def modify_process(decorated_object, num):
#     return decorated_object.process()*num

# class EnclosedAdd:
#     def __init__(self, decorated_object):
#         self.decorated_object = decorated_object

class Multiply:
    def __init__(self, decorated, num):
        self.decorated = decorated
        self.num = num

    def process(self):
        print("I'm a multiply process")
        return self.decorated.process() * self.num

class Divide:
    def __init__(self, decorated, num):
        self.decorated = decorated
        self.num = num

    def process(self):
        print("I'm a divide process")
        return self.decorated.process() / self.num


add_object = Add(2,2)

multiply_add_object = Multiply(add_object, 4)
divide_multiply_add_object = Divide(multiply_add_object, 8)
print(divide_multiply_add_object.process())