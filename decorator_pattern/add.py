# Checking out examples from this article:
# https://medium.com/better-programming/decorator-pattern-and-python-decorators-b0b573f4c1ce


class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def process(self):
        return self.a + self.b