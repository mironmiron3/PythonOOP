class Child:
    def __init__(self,food_cost: int, *toys_cost):
        overall = 0
        for item in toys_cost:
            overall += item
        self.cost = overall + food_cost


