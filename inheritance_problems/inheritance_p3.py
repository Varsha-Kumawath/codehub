class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display_details(self):
        return f"Name: {self.name}\nAge: {self.age}"


class Doctor(Person):

    def __init__(self,name,age,specialization):
        super().__init__(name,age)
        self.specialization=specialization

    def display_details(self):
        return f"{super().display_details()}\nSpecialization: {self.specialization}"


class Patient(Person):

    def __init__(self,name,age,disease):
        super().__init__(name,age)
        self.disease=disease

    def display_details(self):
        return f"{super().display_details()}\nDisease: {self.disease}"

doc=Doctor("varsh",24,"Cardio")
print(doc.display_details())
patient=Patient("Jaga", 24,"Fever")
print(patient.display_details())