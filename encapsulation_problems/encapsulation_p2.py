class student:

    def __init__(self,stud_name,avg=0):

        self.stud_name=stud_name
        self.__grades=[]
        self.avg=avg

    @property
    def display_grade(self):
        return self.__grades.copy()

    def add_grade(self,marks):
        # if (marks>=0 and marks <=100) :
        if 0<= marks <=100:
            self.__grades.append(marks)
            print (f"Grade {marks} added successfully.")
        else:
            print("grades should be between 0-100")

    def avg_grade(self):
        if self.__grades:
            self.avg=sum(self.__grades) /len(self.__grades)
            print (f"Grade {self.avg} calculated successfully.")
            return self.avg

        else:
            print(" No Grades found")


    def is_passed(self):
        if self.avg >=50:
            print(f" {self.stud_name} , Congrulations you are passed with Grade {self.avg}")

        else:
            print( f" {self.stud_name}, Better Luck next time . Your Grade : {self.avg}")




s=student('varsh')
# s.add_grade(50)
# s.add_grade(95)
# s.add_grade(75)
print(s.display_grade)
s.avg_grade()
s.is_passed()


