from food250612 import Food
from drink250612 import Drink

food1 = Food(
    "サンドイッチ",
    500,
)
food1.calorie = 330
print(food1.info())
food1.calorie_info()

drink1 = Drink("コーヒー", 300)
print(drink1.info())
