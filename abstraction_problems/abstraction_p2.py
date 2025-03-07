from abc import ABC,abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class Fan(Appliance):
    def turn_on(self):
        print("Fan is now ON")

    def turn_off(self):
        print("Fan is now OFF")

class Light(Appliance):

    def turn_on(self):
        print("Light is now ON")

    def turn_off(self):
        print("Light is now OFF")


def call_app(appliance_name):
    appliance_name.turn_on()
    appliance_name.turn_off()

app= Fan()
call_app(app)

app2=Light()
call_app(app2)