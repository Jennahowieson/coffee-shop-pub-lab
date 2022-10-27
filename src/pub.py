class Pub:
    def __init__ (self,name,till,drinks):
        self.name = name
        self.till = till
        self.drinks = []
    
    def count_drinks (self):
        return len(self.drinks)
    
    def add_drinks_to_pub (self):
        for drink in src.drink:
            self.drinks += drink 
        return self.drinks