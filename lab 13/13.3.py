class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating):
        self.restaurant_name = restaurant_name  # название рестика
        self.cuisine_type = cuisine_type        # тип кухни
        self.rating = rating                    # рейтинг

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Кухня: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")
        print(" ")

    def update_rating(self, new_rating):
        # обновляем рейтинг ресторана
        self.rating = new_rating
        print(f"Рейтинг ресторана '{self.restaurant_name}' обновлён до {self.rating}")


restaurant1 = Restaurant("Вкусно и Точка", "Русская", 4.5)
restaurant1.describe_restaurant()
restaurant1.update_rating(4.9)
restaurant1.describe_restaurant()