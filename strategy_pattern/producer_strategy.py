from producer_abstract_strategy import DigitalProductionStrategy
from producer_abstract_strategy import AnalogProductionStrategy
from producer_abstract_strategy import AbletonStrategy
from producer_abstract_strategy import FLStrategy

digital = DigitalProductionStrategy()
analog = AnalogProductionStrategy()
ableton = AbletonStrategy()
fl_studio = FLStrategy()

class Producer(object):
    def __init__(self, production_strategy, daw_strategy):
        self._production_strategy = production_strategy
        self._daw_strategy = daw_strategy

    def produce(self):
        self._production_strategy.produce()

    def use_daw(self):
        self._daw_strategy.use_daw()

# Types of producers

class FutureBass(Producer):
    def __init__(self):
        super(FutureBass, self).__init__(digital, ableton)

    def synth(self):
        print('My favorite synth is Serum')

class Trap(Producer):
    def __init__(self):
        super(Trap, self).__init__(digital, fl_studio)

class LABeatScene(Producer):
    def __init__(self):
        super(LABeatScene, self).__init__(analog, ableton)

    def sampler(self):
        print('I love using the SP404')

class QuincyJones(Producer):
    def __init__(self):
        super(QuincyJones, self).__init__(None, None)

    def production_method(self):
        print('I play the piano and record straight to tape!')


print('')
f = FutureBass()
f.produce()
f.use_daw()
f.synth()

print('')
t = Trap()
t.produce()
t.use_daw()

print('')
l = LABeatScene()
l.produce()
l.use_daw()
l.sampler()

print('')
q = QuincyJones()
q.production_method()