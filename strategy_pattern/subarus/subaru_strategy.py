from subaru_abstract_strategy import HigherDriveStrategy
from subaru_abstract_strategy import LowerDriveStrategy
from subaru_abstract_strategy import HeatedSeatsStrategy

high_drive = HigherDriveStrategy()
lower_drive = LowerDriveStrategy()
heated_seats = HeatedSeatsStrategy()

class Subaru(object):
    def __init__(self, drive_strategy, seat_strategy):
        self._drive_strategy = drive_strategy
        self._seat_strategy = seat_strategy

    def drive(self):
        self._drive_strategy.drive()

    def heated_seats(self):
        self._seat_strategy.heated_seats()


class Forester(Subaru):
    def __init__(self):
        super(Forester, self).__init__(high_drive, None)

    def color(self):
        print('I am charcoal')

class Crosstrek(Subaru):
    def __init__(self):
        super(Crosstrek, self).__init__(lower_drive, heated_seats)

    def color(self):
        print("I'm white")

print('')

f = Forester()
f.drive()
f.color()

print('')
c = Crosstrek()
c.drive()
c.heated_seats()
c.color()