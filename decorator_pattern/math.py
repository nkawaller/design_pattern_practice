class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def process(self):
        return self.a + self.b

def modify_process(decorated_object, num):
    return decorated_object.process()*num

add_object = Add(5,5)

print(add_object.process())