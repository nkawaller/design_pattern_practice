import abc

class ProductionStrategyAbstract(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def produce(self):
        """Required Method"""

class DigitalProductionStrategy(ProductionStrategyAbstract):
    def produce(self):
        print("I use sample packs")

class AnalogProductionStrategy(ProductionStrategyAbstract):
    def produce(self):
        print('I use analog synths')

class DAWStrategyAbstract(object):
    @abc.abstractmethod
    def use_daw(self):
        """Required Method"""

class AbletonStrategy(DAWStrategyAbstract):
    def use_daw(self):
        print('I use Ableton')

class FLStrategy(DAWStrategyAbstract):
    def use_daw(self):
        print('I use FL Studio')