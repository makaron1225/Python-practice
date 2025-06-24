from menu_item250612 import MenuItem


class Food(MenuItem):
    def calorie_info(self):
        print(str(self.calorie) + "kcalです")
