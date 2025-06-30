# Определение класса Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} сейчас открыт!")

# Создание экземпляра класса
newRestaurant = Restaurant("Вкусно и Точка", "Русская кухня")

# Вывод атрибутов по отдельности
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)

# Вызов методов
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()