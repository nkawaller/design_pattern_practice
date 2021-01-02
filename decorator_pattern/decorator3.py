class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def process(self):
        return self.a + self.b

# def modify_process(decorated_object, num):
#     return decorated_object.process()*num

# Object enclosing
class EnclosedAdd:
    def __init__(self, decorated_object):
        self.decorated_object = decorated_object

# enclosed it within a decorating object with similar interface
# create a similar interface as class Add
class Multiply:
    def __init__(self, decorated, num):
        self.decorated = decorated
        self.num = num

    def process(self):
        return self.decorated.process() * self.num

ObjectA = Add(2,2)

# print(ObjectA.process())
# print(modify_process(ObjectA,4))
# enclosed_object_A = EnclosedAdd(ObjectA)
multiply_add_object = Multiply(ObjectA, 4)
print(multiply_add_object.process())