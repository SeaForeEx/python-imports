from appliances import Appliance

class DishWasher(Appliance):

    def __init__(self, color):
        super().__init__(color)
        self.color = color

    def wash_dishes(self, color):
        self.color = color
        print("grind, grind, clunk. Time to call the repair person")
        

