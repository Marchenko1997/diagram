from abc import ABC, abstractmethod

class View(ABC):
    @abstractmethod
    def dispaly (self, message: str):
        pass


class ConsoleView(View):
    def display(self, message: str):
        print(message)