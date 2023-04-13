from appliances import Appliance

class Stove(Appliance):

    def __init__(self, color, heat_method="electric"):
        super().__init__(color)
        self.color = color
        self.heat_method = heat_method

    def let_them_cook(self, preheated="yes"):
        if preheated == "yes":
            print("That smells good")
        else:
            print("Let the oven preheat")
