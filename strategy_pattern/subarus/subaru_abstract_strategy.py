import abc

class DriveAbstractStragegy(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def drive(self):
        """Required method"""

class HigherDriveStrategy(DriveAbstractStragegy):
    def drive(self):
        print('I drive higher off the ground')

class LowerDriveStrategy(DriveAbstractStragegy):
    def drive(self):
        print('I drive lower to the ground')

class SeatHeatStrategy(object):
    @abc.abstractmethod
    def heated_seats(self):
        """Required Method"""

class HeatedSeatsStrategy(SeatHeatStrategy):
    def heated_seats(self):
        print('I have heated seats')