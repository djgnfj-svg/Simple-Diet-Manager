from abc import abstractmethod

from common.base_manager import ManagerBase


class MakerBase(ManagerBase):
    def __init__(self, _model):
        super().__init__(_model)

    @abstractmethod
    def make_instance(self):
        pass