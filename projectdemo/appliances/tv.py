from projectdemo.appliances.appliance import Appliance

class Stove(Appliance):
    def __init__(self):
        super().__init__(1.5)