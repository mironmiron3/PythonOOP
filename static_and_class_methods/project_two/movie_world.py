from project_two.customer import Customer
from project_two.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []


    def dvd_capacity(self):
        return 15 - len(self.dvds)

    def customer_capacity(self):
        return 15 - len(self.customers)

    def add_customer(self, customer: Customer):
        if self.customer_capacity() > 0:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if self.dvd_capacity() > 0:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer_object = [customer for customer in self.customers if customer.id == customer_id][0]
        dvd_object = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        if dvd_object in customer_object.rented_dvds:
            return f"{customer_object.name} has already rented {dvd_object.name}"
        elif dvd_object.is_rented:
            return f"DVD is already rented"
        elif customer_object.age < dvd_object.age_restriction:
            return f"{customer_object.name} should be at least {dvd_object.age_restriction} to rent this movie"
        else:
            dvd_object.is_rented = True
            customer_object.rented_dvds.append(dvd_object)
            return f"{customer_object.name} has successfully rented {dvd_object.name}"

    def return_id(self, customer_id, dvd_id):
        customer = [customer for customer in self.customers if customer.id == customer_id][0]
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"
        dvd.is_rented = False
        customer.rented_dvds.remove(dvd)
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        result = []
        for customer in self.customers:
            result.append(repr(customer))
        for dvd in self.dvds:
            result.append(repr(dvd))
        return '\n'.join(result)











c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))

print(movie_world)
