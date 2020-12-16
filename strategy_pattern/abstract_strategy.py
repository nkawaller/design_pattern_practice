import abc

class QuackStrategyAbstract(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def quack(self):
        """Required method"""

class LoudQuackStrategy(QuackStrategyAbstract):
    def quack(self):
        print('QUACK! QUACK!!')

class GentleQuackStrategy(QuackStrategyAbstract):
    def quack(self):
        print('quack, quack')

class LightStrategyAbstract(object):
    @abc.abstractmethod
    def lights_on(self):
        """Required Method"""

class OnForTenSecondsStrategy(LightStrategyAbstract):
    def lights_on(self):
        print('Lights on for 10 seconds')
