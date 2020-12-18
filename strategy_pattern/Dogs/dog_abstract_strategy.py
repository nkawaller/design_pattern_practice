import abc

class BarkStrategyAbstract(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def bark(self):
        """Required Method"""

class LoudBarkStrategy(BarkStrategyAbstract):
    def bark(self):
        print('BARK! BARK!!')

class QuietBarkStrategy(BarkStrategyAbstract):
    def bark(self):
        print('bark...')

class TailWagStrategyAbstract(object):
    @abc.abstractmethod
    def tail_wag(self):
        """Required Method"""

class FastTailWagStrategy(TailWagStrategyAbstract):
    def tail_wag(self):
        print('wag wag wag wag wag')