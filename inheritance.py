import random
class Person :
    def __init__(self , Name , LastName , Major , Phone , Birth):
        self.Name = Name
        self.LastName = LastName
        self.Major = Major
        self.Phone = Phone
        self.Birth = Birth

    def Age(self) :
        year = self.Birth.split("/")[0]
        return 1403 - int(year)
    
    def ShowInfo(self) :
        return f"{self.Name} {self.LastName}"

class Student(Person) :
    stNums = []
    def __init__(self, Name, LastName, Major, Phone, Birth , Grade):
        super().__init__(Name, LastName, Major, Phone, Birth)
        number = random.randint(4030000 , 4039999)
        if number in Student.stNums :
            while number in Student.stNums :
                number = number + 1
            self.StudentNum = number
        else :
            self.StudentNum = number
        self.Units = []
        self.Scores = {}
        self.Grade = Grade

    def ShowInfo(self) :
        return f"{self.Name} {self.LastName} \n 📞  Contact : {self.Phone}"

class Teacher(Person) :
    def __init__(self, Name, LastName, Major, Phone, Birth , isFaculty , Lesson , Grade):
        super().__init__(Name, LastName, Major, Phone, Birth)
        self.isFctualiy = isFaculty
        self.Lesson = Lesson
        self.Grade = Grade

    def ShowInfo(self) :
        return f"{self.Name} {self.LastName} \n ☎️  Contact : {self.Phone}"

######################################################################################

Student1 = Student("Nila" , "Vo" , "Computer" , 989120273410 , "1384/06/27"  , "Associate")
print(Student1.Age())
print(Student1.ShowInfo())

Teacher1 = Teacher("Hamidreza" , "Moghadas" , "IT" , 98360273410 , "1343/10/17" , True , "Network" , "PHD")
print(Teacher1.Age())
print(Teacher1.ShowInfo())