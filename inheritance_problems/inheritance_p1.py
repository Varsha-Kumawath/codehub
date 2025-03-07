class Employee:

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display_details(self):
        print (f" Employee name : {self.name}")
        print(f" Salary : {self.salary}")

class Manager(Employee):

    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus=bonus

    def cal_bonus(self):
        return self.salary+self.bonus

    def display_details(self):
        print(f" Manager name : {self.name}")
        print(f" Salary : {self.salary}")
        print(f" Bonus : {self.cal_bonus()}")

class Developer(Employee):

    def __init__(self, name, salary,programming_lang):
        Employee.__init__(self,name, salary)
        self.programming_lang = programming_lang

    def display_details(self):
        print (f" Developer name : {self.name}")
        print(f" Salary : {self.salary}")
        print(f" programming Language : {self.programming_lang}")



emp=Employee("varsha",30000)
emp.display_details()

Man=Manager("varsha",30000, 5000)
Man.cal_bonus()
Man.display_details()

Dev=Developer("varsha",30000, "python")
Dev.display_details()