from appliances.kitchen.utility.dishwasher import DishWasher
from appliances.laundry.dryer import Dryer
from appliances.laundry.washer import Washer
from appliances.kitchen.utility.refrigerator import Refrigerator
from appliances.kitchen.coffeemaker import CoffeeMaker
from appliances.kitchen.stove import Stove
from appliances.kitchen.can_opener import CanOpener

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes("red")

samsung_washer = Washer("red", "normal")
samsung_washer.wash_clothes()
samsung_dryer = Dryer("red", "gas")
samsung_dryer.dry_clothes()

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

gen_electric = Stove("blue", "electric")
gen_electric.let_them_cook()

jon_arbuckle = CanOpener("blue")
jon_arbuckle.open_can()
