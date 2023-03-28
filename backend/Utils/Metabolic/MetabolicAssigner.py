from Utils.common.AssginerBase import AssignerBase
from Utils.Metabolic.MetabolicCalculator import Metabolic_Carculater

class Metabolic_Assigner(AssignerBase):
    def __init__(self):
        self.protein_range = 1.8
        self.fat_range = 0.3
        super().__init__()

    def assign_data(self, data):
        '''
            {
                'age': 20,
                'weight': 80.0,
                'height': 170.0,
                'gender': 'M',
                'general_activities': 1.2,
                'excise_activity': 0.2,
                'meal_count': 3
            }
        '''
        self.total_kcal = Metabolic_Carculater.calculate_kcal(data)
        self.total_protein = Metabolic_Carculater.calculate_protein(data,self.protein_range)
        self.total_fat = Metabolic_Carculater.calculate_fat(self.total_kcal,self.fat_range)
        self.total_carbs = Metabolic_Carculater.calculate_carbs(self.total_kcal,self.total_protein,self.total_fat)

    def get_data_dict(self):
        return {
            'total_kcal': self.total_kcal,
            'total_carbs': self.total_carbs,
            'total_protein': self.total_protein,
            'total_fat': self.total_fat
        }
