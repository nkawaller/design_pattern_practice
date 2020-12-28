from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ConcreteWeatherStation(Subject):

    _state: int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print('Weather Station: Attached an observer.')
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print('Weather Station: Notifying observers...')
        for observer in self._observers:
            observer.update(self)

    def some_weather_calculations(self) -> None:
        print("\nWeather Station: I'm gathering weather data.")
        self._state = randrange(0,10)

        print(f"Weather Station: My state has just changed")
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass

class HomeDisplayA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("HomeDisplayA: Reacted to the weather data")

class HomeDisplayB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("HomeDisplayB: Reacted to the weather data")


if __name__ == '__main__':

    weather_station = ConcreteWeatherStation()

    home_display_a = HomeDisplayA()
    weather_station.attach(home_display_a)

    home_display_b = HomeDisplayB()
    weather_station.attach(home_display_b)

    weather_station.some_weather_calculations()
    weather_station.some_weather_calculations()

    weather_station.detach(home_display_a)

    weather_station.some_weather_calculations()
