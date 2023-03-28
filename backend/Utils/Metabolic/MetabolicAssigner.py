from Utils.common.AssginerBase import AssignerBase


class Metabloic_Assigner(AssignerBase):
    def __init__(self):
        self.total_carbs = 0
        self.total_protein = 0
        self.total_fat = 0
        self.total_kcal = 0
        super().__init__()

    def assign_data(self, data):
        print(data)
        pass