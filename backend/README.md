# 코드 설명




# Common
 - 식단과 식사를 만드는 데 필요한 getter와 maker가 있습니다.
 ## getter - 정보와 같은 데이터를 가져오는 역할을 합니다.
 ```
class GetterBase(ManagerBase):
    def __init__(self, _model):
        super().__init__(_model)

    @abstractmethod
    def get_data(self):
        pass

    def find_instance(self, model, min_nutrient, max_nutrient, meal_count=None, category=None):
        q = Q()

        for nutrient in ["kcal", "protein", "fat", "carbs"]:
            nutrient_min = "{}".format(nutrient)
            nutrient_max = "{}".format(nutrient)
            q &= Q(**{"{}__gte".format(nutrient_min): min_nutrient[nutrient], "{}__lte".format(nutrient_max): max_nutrient[nutrient]})
            if category is not None:
                q &= Q(category=category)
            if meal_count is not None:
                q &= Q(meal_count=meal_count)
        return model.objects.filter(q)
 ```
 ## maker - 정보와 같은 데이터가 없다면 만드는 역할을 합니다.
 ```
 class MakerBase(ManagerBase):
    def __init__(self, _model):
        super().__init__(_model)

    @abstractmethod
    def make_instance(self):
        pass
 ```
 
# Core
- 기초대사량과 영양소를 계산하는 로직들이 있습니다.

# API
## View
- 인터페이스 처럼 사용하며 대표적으로 다음과 같이 사용했습니다.
```
class FoodCategoryViewset(viewsets.ModelViewSet):
    serializer_class = FoodCategorySerializer

    def get_queryset(self):
        return FoodCategory.objects.order_by("-id").exclude(name="기타")

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
```
## Serializer
- 데이터의 형태를 정의하는 역할을 합니다. 그 데이터를 core의 로직을 통해 만들거나 가져옵니다.
```
class MealSerializer(serializers.ModelSerializer):
    foods = serializers.PrimaryKeyRelatedField(many=True, queryset=Food.objects.all())
    
    kcal = serializers.IntegerField(read_only=True, default=0)
    protein = serializers.IntegerField(read_only=True, default=0)
    fat = serializers.IntegerField(read_only=True, default=0)
    carbs = serializers.IntegerField(read_only=True, default=0)
    
    class Meta:
        model = Meal
        exclude = ('created_at', 'updated_at')
        
    def to_representation(self, instance):
        rtn = super().to_representation(instance)
        rtn['foods'] = FoodSerializer(instance.foods.all(), many=True).data
        return rtn
    
    def validate(self, data):
        if 'foods' not in data:
            raise serializers.ValidationError("foods field is required")
        return data
    
    def create(self, validated_data):
        instance = Meal.objects.meal_create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        try:
            instance = Meal.objects.meal_update(**validated_data)
        except ValueError as e:
            raise serializers.ValidationError(str(e))
        return instance
```