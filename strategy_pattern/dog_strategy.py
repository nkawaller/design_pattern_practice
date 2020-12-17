from abs import LoudBarkStrategy
from abs import QuietBarkStrategy
from abs import FastTailWagStrategy

loud_bark = LoudBarkStrategy()
quiet_bark = QuietBarkStrategy()
tail_wag = FastTailWagStrategy()


class Dog(object):
    def __init__(self, bark_strategy, tail_wag_strategy):
        self._bark_strategy = bark_strategy
        self._tail_wag_strategy = tail_wag_strategy

    def bark(self):
        self._bark_strategy.bark()

    def tail_wag(self):
        self._tail_wag_strategy.tail_wag()

# Types of Dogs

class Doberman(Dog):
    def __init__(self):
        super(Doberman, self).__init__(loud_bark, None)

    def go_home(self):
        print('I live in a big house')

class GermanShepherd(Dog):
    def __init__(self):
        super(GermanShepherd, self).__init__(loud_bark, None)

    def go_home(self):
        print('I live in a fairly large house')

class Pug(Dog):
    def __init__(self):
        super(Pug, self).__init__(quiet_bark, tail_wag)

    def go_home(self):
        print('I live in a small house')

class Beagle(Dog):
    def __init__(self):
        super(Beagle, self).__init__(loud_bark, tail_wag)

p = Beagle()
p.bark()
p.tail_wag()