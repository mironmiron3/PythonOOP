from projectdemo.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, pension_one+pension_two, 2)
        self.room_cost = 15
        self.list_of_appliances = ["tv","fridge","stove"]
        sum = 0
        for item in self.list_of_appliances:
            if item == "tv":
                sum += 1.5 * 30 * 2
            elif item == "laptop":
                sum += 1 * 30 * 2
            elif item == "fridge":
                sum += 1.2 * 30 * 2
            elif item == "stove":
                sum += 0.7 * 30 * 2
        self.expenses = sum
