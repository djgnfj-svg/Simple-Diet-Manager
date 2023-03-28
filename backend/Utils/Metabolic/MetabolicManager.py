from Utils.Metabolic.MetabolicAssigner import Metabloic_Assigner
from Utils.common.ManagerBase import ManagerBase


class Metabolic_Manager(ManagerBase):
    def __init__(self):
        super().__init__()

    def assign_data(self, data):
        Metabloic_Assigner.assign_data(data)
        return
    
    def get_data(self):
        return super().get_data()