from abc import *

class ManagerBase(metaclass=ABCMeta):
    def __init__(self):
        pass
    
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def assign_data(self, data):
        pass