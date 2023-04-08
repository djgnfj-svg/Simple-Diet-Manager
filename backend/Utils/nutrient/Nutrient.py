

# 영양소 계산기
class NutrientCalculator:

    # range 계산기
    @staticmethod
    def cal_range(value, range):
        return round(value * range)
    
    # return dict
    def _cal_nutrient_range(self, data, range):
        rtn = {}
        rtn["kcal"] = self._cal_range(data["metabolism_kcal"], range)