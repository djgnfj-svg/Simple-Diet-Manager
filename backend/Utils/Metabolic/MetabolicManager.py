from Utils.common.ManagerBase import ManagerBase
from Utils.Metabolic.MetabolicCalculator import Metabolic_Carculater

class Metabolic_Manager(ManagerBase):
    def __init__(self):
        self.data = {}
        self.protein_range = 1.8
        self.fat_range = 0.3

    def get_data(self, data):
        self.data["total_kcal"] = Metabolic_Carculater.calculate_kcal(data)
        self.data["total_protein"] = Metabolic_Carculater.calculate_protein(data,self.protein_range)
        self.data["total_fat"] = Metabolic_Carculater.calculate_fat(self.data["total_kcal"],self.fat_range)
        self.data["total_carbs"] = Metabolic_Carculater.calculate_carbs(self.data["total_kcal"], self.data["total_protein"], self.data["total_fat"])

        return self.data
    