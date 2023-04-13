from appliances import Appliance

class CanOpener(Appliance):

    def __init__(self, color):
        super().__init__(color)
        self.color = color

    def open_can(self, ishungry=True):
        if ishungry == True:
            print("Tuna smells bad")
        else:
            print("Go to next python exercise")
