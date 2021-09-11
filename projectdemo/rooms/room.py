from projectdemo.appliances.appliance import Appliance
from projectdemo.people.child import Child

class Room:
    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        #self.expenses = 0
        
    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")

        self.__expenses = value

    def calculate_expenses(self,*args):
        sum = 0
        for each_list in args:
            for item in each_list:
                sum += item.cost
        sum *= 30
        self.__expenses = sum

#child1 = Child(5,2,3)
#child2 = Child(1,1)
#appliance = Appliance(2)
#room = Room("Ivancghev", 20, 5)
#room.calculate_expenses([child1,child2],[appliance])
#print(room.expenses)

