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

