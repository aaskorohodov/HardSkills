from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, action):
        pass


class Observable:
    def __init__(self):
        """_observers stores any class, that should be notified"""

        self._observers = []

    def notify(self, *args):
        """Notifies all observers"""

        for observer in self._observers:
            observer.update(*args)

    def attach(self, observer):
        """Attaches new observer to the notification system"""

        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """You guessed it"""

        if observer in self._observers:
            self._observers.remove(observer)
