from abc import *


class ManagerBase(metaclass=ABCMeta):
    def __init__(self, _model):
        self.model = _model