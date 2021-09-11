class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self,room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_expenses = 0
        for room in self.rooms:
            total_expenses += room.room_cost + room.expenses
        return f"Monthly consumption: {total_expenses}$."

    def pay(self):
        result = []
        for room in self.rooms:
            if room.budget >= room.expenses + room.room_cost:
                result.append(f"{room.family_name} paid {room.expenses+room.room_cost}$ and have {room.budget-(room.expenses+room.room_cost)}$ left.")
            else:
                name = room.family_name
                del room
                result.append(f"{name} does not have enough budget and must leave the hotel.")
        return "/n".join(result)

    def status(self):
        pass


