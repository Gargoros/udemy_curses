class Pizza:
    order_number = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.order_number += 1
        Pizza.order_number += 1

    def ingredients(ingredients):
        return ingredients
        
    @classmethod
    def hawaiian(cls):
        return cls(ingredients = ["ham", "pineapple"])
    
    @classmethod
    def meat_festival(cls):
        return cls(ingredients = ["beef", "meatball", "bacon"])
    
    @classmethod
    def garden_feast(cls):
        return cls(ingredients = ["spinach", "olives", "mushroom"])