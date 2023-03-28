from Utils.common.ManagerBase import ManagerBase
from diet.DietAssigner import Diet_Assigner


class Diet_Manager(ManagerBase):
    def __init__(self, data):
        _Diet = Diet_Assigner()
        _Diet.assign_data(data)
        self.data = _Diet.get_data()

    def get_data(self):
        return self.data