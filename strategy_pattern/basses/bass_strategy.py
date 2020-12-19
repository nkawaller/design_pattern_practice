from bass_abstract_strategy import AcousticStrategy
from bass_abstract_strategy import ElectricStrategy
from bass_abstract_strategy import FourStringStrategy

acoustic_bass = AcousticStrategy()
electric_bass = ElectricStrategy()
string_number = FourStringStrategy()


class Bass(object):
    def __init__(self, sound_strategy, string_number_strategy):
        self._sound_strategy = sound_strategy
        self._string_number_strategy = string_number_strategy

    def sound(self):
        self._sound_strategy.sound()

    def string_number(self):
        self._string_number_strategy.string_number()


# Types of basses

class EighteenFiftyGerman(Bass):
    def __init__(self):
        super(EighteenFiftyGerman, self).__init__(acoustic_bass, string_number)

class Sadowsky(Bass):
    def __init__(self):
        super(Sadowsky, self).__init__(electric_bass, string_number)

class FBass(Bass):
    def __init__(self):
        super(FBass, self).__init__(electric_bass, None)

    def low_b(self):
        print ('I also have a low b string')

class ThundercatBass(Bass):
    def __init__(self):
        super(ThundercatBass, self).__init__(None, None)

    def description(self):
        print("I'm a six-string acoustic-electric")

print('')
e = EighteenFiftyGerman()
e.sound()
e.string_number()

print('')
s = Sadowsky()
s.sound()
s.string_number()

print('')
f = FBass()
f.sound()
f.low_b()

print('')
t = ThundercatBass()
t.description()