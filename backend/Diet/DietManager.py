

from Utils.common.ManagerBase import ManagerBase


class Diet_Manager(ManagerBase):
    def __init__(self):
        super().__init__()

    def assign_data(self, data):
        Diet_Assigner.assign_data(data)
        return
    
    def get_data(self):
        return super().get_data()