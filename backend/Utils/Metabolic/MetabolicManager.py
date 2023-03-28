from Utils.Metabolic.MetabolicAssigner import Metabolic_Assigner
from Utils.common.ManagerBase import ManagerBase


class Metabolic_Manager(ManagerBase):
    def __init__(self, data):
        _Metabolic = Metabolic_Assigner()
        _Metabolic.assign_data(data)
        self.data = _Metabolic.get_data_dict()

    def get_data(self):
        return self.data
    