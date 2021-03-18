prices = {"Strawberries" : 1.5, "Banana" : 0.5, 
          "Mango" : 2.5, "Blueberries" : 1, 
          "Raspberries" : 1, "Apple" : 1.75, 
          "Pineapple" : 3.5}

class Beverage:
    
    def __init__(self, ingredients):
        self.ingredients = ingredients 
        
    def ingredients():
        return ingredients
        
    def get_cost(self):
        self.cost = []
        for name1, price in prices.items():
            for name2 in self.ingredients:
                if name1 == name2:
                    self.cost.append(prices[name2])
        return f"${sum(self.cost)}"
        
    def get_price(self):
        self.price = sum(self.cost) * 2.5
        return f"${self.price}"        
        
    def get_name(self):
        self.name = " ".join(self.ingredients)
        self.new_name = self.name.replace("berries", "berry")
        if len(self.ingredients) > 1:
            return (self.new_name + " Fusion")
        else:
            return (self.new_name + " Smoothie")
            
        
        
s = Beverage(["Banana", "Apple"])
print(s.ingredients)
print(s.get_cost())
print(s.get_price())
print(s.get_name())
