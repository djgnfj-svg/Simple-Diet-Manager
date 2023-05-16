from config.nutrient_range import FAT_RANGE, PROTEIN_RANGE
from core.metabolic_calculator import MetabolicCarculater


class MetabolicManager:
    def __init__(self):
        self.data = {}

    def make_metabolic_data(self, data):
        self.data["kcal"] = MetabolicCarculater.calculate_kcal(data)
        self.data["protein"] = MetabolicCarculater.calculate_protein(data, PROTEIN_RANGE)
        self.data["fat"] = MetabolicCarculater.calculate_fat(self.data["kcal"], FAT_RANGE)
        self.data["carbs"] = MetabolicCarculater.calculate_carbs(self.data["kcal"], self.data["protein"], self.data["fat"])

        return self.data
    