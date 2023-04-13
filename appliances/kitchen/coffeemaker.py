from appliances import Appliance

class CoffeeMaker(Appliance):

    def __init__(self, color):
        super().__init__(color)
        self.color = color

    def make_coffee(self, beans="none"):
        if beans != "none":
            print("gurgle, gurgle. Ding. Your drug of choice is piping hot and ready!")
        else:
            print("Go to starbucks or chug a MONSTER!!!")
