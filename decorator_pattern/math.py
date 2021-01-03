class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def process(self):
        return self.a + self.b

# Enclose it within a decorating object with a similar interface
class EnclosedAdd:
    def __init__(self, decorated_object):
        print("I'm wrapping the add object")
        self.decorated_object = decorated_object

add_object = Add(5,5)
enclosed_add_object = EnclosedAdd(add_object)
print(enclosed_add_object)