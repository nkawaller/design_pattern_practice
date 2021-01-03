class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def process(self):
        return self.a + self.b

# Enclose it within a decorating object with a similar interface
class EnclosedAdd:
    def __init__(self, decorated_object, num):
        print("I'm wrapping the add object")
        self.decorated_object = decorated_object
        self.num = num

    def process(self):
        return self.decorated_object.process() * self.num

class Divide:
    def __init__(self.decorated_object, num):
        self.decorated_object = decorated_object
        self.num = num

    def process(self):
        print("I'm a divide process")
        return self.decorated_object.process() // self.num

add_object = Add(5,5)
enclosed_add_object = EnclosedAdd(add_object, 5)
print(enclosed_add_object.process())