
class Bar:

    # Advanced Extensions 2..

    def __init__(self):
        self.drinks = []
        self.tab = 0

    def add_drink(self, drink):
        self.drinks.append(drink)

    def increase_tab_by_drink(self, drink):
        self.tab += drink.price

    def print_tab(self):
        return self.tab

    def print_itemised_tab(self):
        return self.drinks

        
        

