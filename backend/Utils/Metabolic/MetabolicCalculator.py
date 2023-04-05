
class MetabolicCarculater():
    def __init__(self):
        pass

    @staticmethod
    def calculate_kcal(data):
        age = data["age"]
        gender = data["gender"]
        weight = data["weight"]
        height = data["height"]
        general_activity = data["general_activity"]
        excise_activity = data["excise_activity"]

        # 기초대사량
        if gender == "M":
            basal_metabolic_rate = 88.4 + (13.4 * weight) + \
                (4.8 * height) - (5.68 * age)
        else:
            basal_metabolic_rate = 447.6 + (9.25 * weight) + \
                (3.1 * height) - (4.33 * age)
        activity_coefficient = general_activity + excise_activity

        total_kcalorie = round(basal_metabolic_rate * activity_coefficient)
        return total_kcalorie

    @staticmethod
    def calculate_protein(data, protein_range=1.6):
        total_protein = round(data["weight"] * protein_range)
        return total_protein

    @staticmethod
    def calculate_fat(total_kcal, fat_range=0.3):
        total_fat = round(total_kcal * fat_range / 9)
        return total_fat

    @staticmethod
    def calculate_carbs(toal_kcal, total_protein, total_fat):
        total_carbs = round((toal_kcal - (total_protein * 4) - (total_fat * 9)) / 4)
        return total_carbs
