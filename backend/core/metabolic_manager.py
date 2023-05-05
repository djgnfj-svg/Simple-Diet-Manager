from common.manager.base_manager import ManagerBase
from config.nutrient_range import FAT_RANGE, PROTEIN_RANGE
from core.metabolic_calculator import MetabolicCarculater


class MetabolicManager(ManagerBase):
    def __init__(self):
        self.data = {}

    def get_data(self, data):
        self.data["metabolism_kcal"] = MetabolicCarculater.calculate_kcal(data)
        self.data["metabolism_protein"] = MetabolicCarculater.calculate_protein(data, PROTEIN_RANGE)
        self.data["metabolism_fat"] = MetabolicCarculater.calculate_fat(self.data["metabolism_kcal"], FAT_RANGE)
        self.data["metabolism_carbs"] = MetabolicCarculater.calculate_carbs(self.data["metabolism_kcal"], self.data["metabolism_protein"], self.data["metabolism_fat"])

        return self.data
    