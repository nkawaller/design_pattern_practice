import abc

class SoundProductionStrategyAbstract(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def sound(self):
        """Required Method"""

class AcousticStrategy(SoundProductionStrategyAbstract):
    def sound(self):
        print('Sound resonates in a large carved-maple body with a spruce top')

class ElectricStrategy(SoundProductionStrategyAbstract):
    def sound(self):
        print('Vibrations are picked up by wound pickups')

class StringNumberStrategyAbstract(object):
    @abc.abstractmethod
    def string_number(self):
        """Required Method"""

class FourStringStrategy(StringNumberStrategyAbstract):
    def string_number(self):
        print("I'm a four-string bass")