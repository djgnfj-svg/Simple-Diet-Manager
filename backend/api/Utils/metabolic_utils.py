

from core.metabolic_manager import MetabolicManager
from core.nutrient_utils import cal_nutrient_range, get_min_max_range


def make_min_max_nutrient(validated_data):
    metabolic_manager = MetabolicManager()
    metabolic = metabolic_manager.make_metabolic_data(validated_data)
    min_range, max_range = get_min_max_range(validated_data['diet_status'])
    min_nutrient = cal_nutrient_range(metabolic, min_range)
    max_nutrient = cal_nutrient_range(metabolic, max_range)

    return min_nutrient, max_nutrient