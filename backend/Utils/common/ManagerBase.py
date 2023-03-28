from abc import *

class ManagerBase(metaclass=ABCMeta):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def get_data(self):
        return self.data