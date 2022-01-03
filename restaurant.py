class Restaurant(): 
    def __init__(self, restaurant, cuisine): 
        self.restaurant_name = restaurant 
        self.cuisine_type = cuisine 

    def describe_restaurant(self): 
        print(f"The {self.restaurant_name} restaurant sell {self.cuisine_type} food.") 

    def open_restaurant(self): 
        print(f"The {self.restaurant_name} restaurant is Open.") 


class IceCreamStand(Restaurant):
    def __init__(self, restaurant, cuisine):
        super().__init__(restaurant, cuisine)
        self.mobility = True

    def ice_cream_flavors(self, *flavors):
        list_flavors = []
        print(f"The flavors of ice cream:")
        for flavor in flavors:
            print(f'- {flavor}')
            list_flavors.append(flavor)
        print(f'The all flavors: {list_flavors}')
            

a = Restaurant('KFC', 'Fry Chicken') 
b = Restaurant('Lottle', 'Chicken') 
a.describe_restaurant() 
b.describe_restaurant() 
a.open_restaurant() 
b.open_restaurant()

print('\nTesting child class....')
my_ice_cream = IceCreamStand('ICR', 'Ice Cream')
my_ice_cream.describe_restaurant()
my_ice_cream.open_restaurant()
my_ice_cream.ice_cream_flavors('Sugar', 'Matcha', 'Siro', 'Cheese')