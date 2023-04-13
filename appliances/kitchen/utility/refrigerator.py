from appliances import Appliance


class Refrigerator(Appliance):

    def __init__(self, color):
        super().__init__(color)
        self.color = color

    def make_ice(self, broken=False):
        if broken == True:
            print("grind, grind, clunk. Time to call the repair person")
        else:
            print("time for some ice!")
