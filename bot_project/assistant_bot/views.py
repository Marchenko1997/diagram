from abc import ABC, abstractmethod

class View(ABC):
    @abstractmethod
    def display (self, message: str):
        pass


class ConsoleView(View):
    def display(self, message: str):
        print(message)