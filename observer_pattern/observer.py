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


class ConcreteSubject(Subject):

    _state: int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print('Subject: Attached an observer.')
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print('Subject: Notifying observers...')
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        print("\nSubject: I'm doing some business logic")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass

class FirstConcreteObserver(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("FirstConcreteObserver: Reacted to the event")

class SecondConcreteObserver(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("SecondConcreteObserver: Reacted to the event")

if __name__ == '__main__':

    subject = ConcreteSubject()

    first_observer = FirstConcreteObserver()
    subject.attach(first_observer)

    second_observer = SecondConcreteObserver()
    subject.attach(second_observer)

    subject.some_business_logic()
    subject.some_business_logic()           