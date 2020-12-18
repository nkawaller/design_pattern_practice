from abstract_strategy import LoudQuackStrategy
from abstract_strategy import GentleQuackStrategy
from abstract_strategy import OnForTenSecondsStrategy

loud_quack = LoudQuackStrategy()
gentle_quack = GentleQuackStrategy()
ten_seconds = OnForTenSecondsStrategy()

class Duck(object):
    def __init__(self, quack_strategy, light_strategy):
        self._quack_strategy = quack_strategy
        self._light_strategy = light_strategy

    def quack(self):
        self._quack_strategy.quack()

    def lights_on(self):
        self._light_strategy.lights_on()

# Types of ducks

class VillageDuck(Duck):
    def __init__(self):
        super(VillageDuck, self).__init__(loud_quack, None)

    def go_home(self):
        print('Going to the river')


class ToyDuck(Duck):
    def __init__(self):
        super(ToyDuck, self).__init__(gentle_quack, ten_seconds)

class CityDuck(Duck):
    def __init__(self):
        super(CityDuck, self).__init__(gentle_quack, None)

    def go_home(self):
        print('Going to the central park pond')

class RobotDuck(Duck):
    def __init__(self):
        super(RobotDuck, self).__init__(loud_quack, ten_seconds)

robo = RobotDuck()

robo.quack()
robo.lights_on()