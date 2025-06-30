class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name  # название ресторана
        self.cuisine_type = cuisine_type        # тип кухни

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Кухня: {self.cuisine_type}")
        print(" ")

restaurant1 = Restaurant("Вкусно и Точка", "Русская")
restaurant2 = Restaurant("Токио", "Японская")
restaurant3 = Restaurant("Мама Рома", "Итальянская")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()