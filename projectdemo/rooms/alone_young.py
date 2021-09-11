from projectdemo.rooms.room import Room

class AloneYoung(Room):
    def __init__(self,family_name: str, salary: float):
        super().__init__(family_name,salary,1)
        self.room_cost = 10
        self.list_of_appliances = ["tv"]
        sum = 0
        for item in self.list_of_appliances:
            if item == "tv":
                sum += 1.5 * 30
            elif item == "laptop":
                sum += 1 * 30
            elif item == "fridge":
                sum += 1.2 * 30
            elif item == "stove":
                sum += 0.7 * 30
        self.expenses = sum


