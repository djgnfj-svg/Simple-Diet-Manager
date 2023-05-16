

# 영양소 계산기
class NutrientCalculator:
    # range 계산기
    @staticmethod
    def cal_range(value, range):
        return round(value * range)
    
    @staticmethod
    def cal_min_max_range(diet_status):
        '''
        0 : 감량
        1 : 유지
        2 : 증량 TODO : 미구현
        '''

        if diet_status == 0:
            return 0.8, 0.9
        elif diet_status == 1:
            return 0.9, 1.0