class Vehicle():

    def __init__(self,brand,model,rent_per_day=0):
        self.brand = brand
        self.model=model
        self.rent_per_day=rent_per_day

    def rented_cost(self,days):
        return self.rent_per_day * days

class Car(Vehicle):

    def __init__(self,brand,model,seats):
        super().__init__(brand,model,rent_per_day=1200)
        self.seats=seats



    def rented_cost(self,days):
            return f" Car Rented amount to pay :: {super().rented_cost(days)}"


class Bike(Vehicle):

    def __init__(self, brand, model,gear):
        super().__init__(brand, model,rent_per_day=900)
        self.gear = gear

    def rented_cost(self, days):
             return f" Bike Rented amount to pay :: {super().rented_cost(days)}"


c=Car("prosche", "porsche 911",4)
print(c.rented_cost(2))
b=Bike("Yamaha", "MT-07", 6)
print(b.rented_cost(1))



