from abc import *

class AssignerBase(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def assign_data(self, data):
        pass