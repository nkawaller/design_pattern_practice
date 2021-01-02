class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def process(self):
        return self.a + self.b

def modify_process(decorated_object, num):
    return decorated_object.process()*num

ObjectA = Add(2,2)

print(ObjectA.process())
print(modify_process(ObjectA,4))