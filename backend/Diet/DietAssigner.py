
from Utils.common.AssginerBase import AssignerBase
from Utils.Metabolic.MetabolicManager import Metabolic_Manager


class Diet_Assigner(AssignerBase):
    def __init__(self):
        super().__init__()

    def assign_data(self, data):
        metabolic_manager = Metabolic_Manager()
        metabolic_manager.assign_data(data)
        self.metabolic_data = metabolic_manager.get_data()
    
    def get_data(self):
        return self.metabolic_data