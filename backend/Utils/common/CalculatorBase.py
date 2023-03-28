from abc import *

class CalculatorBase(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def calculate(self, data):
        pass