from project_four.customer import Customer
from project_four.equipment import Equipment
from project_four.exercise_plan import ExercisePlan
from project_four.subscription import Subscription
from project_four.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []


    def add_customer(self, customer: Customer):
         if customer not in self.customers:
             self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
         if trainer not in self.trainers:
             self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
         if equipment not in self.equipment:
             self.equipment.append(equipment)
    def add_plan(self, plan: ExercisePlan):
         if plan not in self.plans:
             self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
         if subscription not in self.subscriptions:
             self.subscriptions.append(subscription)

    @staticmethod
    def get_object(object_id, class_iterable):
        object = list(filter(lambda x: x.id == object_id, class_iterable))[0]
        return object

    def subscription_info(self, subscription_id: int):
        result = []
        subscription = [sub for sub in self.subscriptions if sub.id == subscription_id][0]
        result.append(repr(subscription))
        customer_id = subscription.customer_id
        customer = [customer for customer in self.customers if customer.id == customer_id][0]
        result.append(repr(customer))
        trainer_id = subscription.trainer_id
        trainer = [trainer for trainer in self.trainers if trainer.id == trainer_id]
        result.append(repr(trainer))
        exercise_id = subscription.exercise_id
        exercise = [exercise for exercise in self.plans if exercise.id == exercise_id][0]
        result.append(repr(exercise))
        equipment_id = exercise.equipment_id
        #equipment = [equipment for equipment in self.equipment if equipment.id == equipment_id][0]
        #equipment = list(filter(lambda equipment: equipment.id == equipment_id, self.equipment))[0]
        equipment = Gym.get_object(equipment_id, self.equipment)
        result.append(repr(equipment))
        return '\n'.join(result)


customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))
