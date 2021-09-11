from project.supply.food_supply import FoodSupply
from project.supply.water_supply import WaterSupply
from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve


class Bunker:

    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []
        #self.food = []
        #self.water = []
        #self.painkiller = []
        #self.salves = []
        
    @property
    def food(self):
        result = [item for item in self.supplies if isinstance(item, FoodSupply)]
        if result:
            return result
        raise IndexError("There are no food supplies left!")

    @property
    def water(self):
        result = [item for item in self.supplies if isinstance(item, WaterSupply)]
        if result:
            return result
        raise IndexError("There are no water supplies left!")

    @property
    def painkillers(self):
        result = [item for item in self.medicine if isinstance(item, Painkiller)]
        if result:
            return result
        raise IndexError("There are no painkillers left!")

    @property
    def salves(self):
        result = [item for item in self.medicine if isinstance(item, Salve)]
        if result:
            return result
        raise IndexError("There are no salves left!")

    def add_survivor(self,survivor):
        if survivor not in self.survivors:
            self.survivors.append(survivor)
        else:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")

    def add_supply(self,supply):
        self.supplies.append(supply)

    def add_medicine(self,medicine):
        self.medicine.append(medicine)

    def heal(self,survivor,medicine_type):
        chosen_medicine = None
        if medicine_type.lower() == "painkiller":
            chosen_medicine = self.painkillers.pop()
        if medicine_type.lower() == "salve":
            chosen_medicine = self.salves.pop()
        try:
            chosen_medicine.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"
        except ValueError:
            pass

    def sustain(self, survivor, supply_type):
        chosen_supply = None
        if supply_type.lower() == "food":
            chosen_supply = self.food.pop()
        if supply_type.lower() == "water":
            chosen_supply = self.water.pop()
        try:
            chosen_supply.apply(survivor)
            return f"{survivor.name} healed successfully with {supply_type}"
        except ValueError:
            pass

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            self.add_supply(WaterSupply())
            self.add_supply(FoodSupply())