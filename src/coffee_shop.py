class CoffeeShop:
    def __init__(self,name,till):
        self.name = name
        self.till = till

    def increase_till (self, incoming_cash):
        self.till += incoming_cash