from Utils.common.ManagerBase import ManagerBase
from Utils.Metabolic.MetabolicCalculator import MetabolicCarculater

class MetabolicManager(ManagerBase):
    def __init__(self):
        self.data = {}
        self.protein_range = 2.2
        self.fat_range = 0.3

    def get_data(self, data):
        self.data["metabolism_kcal"] = MetabolicCarculater.calculate_kcal(data)
        self.data["metabolism_protein"] = MetabolicCarculater.calculate_protein(data,self.protein_range)
        self.data["metabolism_fat"] = MetabolicCarculater.calculate_fat(self.data["metabolism_kcal"],self.fat_range)
        self.data["metabolism_carbs"] = MetabolicCarculater.calculate_carbs(self.data["metabolism_kcal"], self.data["metabolism_protein"], self.data["metabolism_fat"])

        return self.data
    