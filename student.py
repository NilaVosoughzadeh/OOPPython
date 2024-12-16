import random

class Student :
    Info = {}
    stNums = []
    def __init__(self , Name , LName , Grade , Major , Phone , Birth):
        self.Name = Name
        self.LName = LName
        self.Grade = Grade
        self.Major = Major
        self.Phone = Phone
        self.Scores = {}
        self.Birth = Birth
        self.Units = []
        number = random.randint(4030000 , 4039999)
        if number in Student.stNums :
            while number in Student.stNums :
                number = number + 1
            self.StudentNum = number
        else :
            self.StudentNum = number
    
    def ShowInfo(self) : 
        return f"{self.Name} {self.LName} - Phone : {self.Phone} - {self.Grade}.{self.Major} - Birthday : {self.Birth} - {self.StudentNum} "
    
    def ChooseUnit(self , Lesson) :
        self.Units.append(Lesson)

    def Age(self) :
        year = self.Birth.split("/")[0]
        return 1403 - int(year)
    
    def ShowAVG(self) :
        return sum(self.Scores.values()) / len(self.Scores.values())
###########################################
class Teacher :
    def __init__(self , Name , LastName , isFaculty , Major , Lesson):
        self.Name = Name
        self.LastName = LastName
        self.isFctualiy = isFaculty
        self.Major = Major
        self.Lesson = Lesson
        self.scores = []

    def SetScore(self , student : Student , Score) :
        student.Scores[self.Lesson] = Score
        self.scores.append(Score)
        Student.Info[self.Lesson] = self.scores
###########################################

Student1 = Student("Nila" , "Vo" , "Associate" , "Computer Software" , 989120273410 , "1384/06/27")

print(Student1.ShowInfo())
print(Student1.Age())

Student1.ChooseUnit("Mabani")
Student1.ChooseUnit("Farsi")
print(Student1.Units)

Student2 = Student("Zoha" , "Ah" , "Associate" , "Computer Software" , 989120278562 , "1383/11/05")
while True :
    Unit = input("Choose your unit : ")
    print("If you want to exit just type it")
    if Unit == "exit" :
        break
    else :
        Student2.ChooseUnit(Unit)

print(Student2.Units)
print(Student2.Age())
Student2.ChooseUnit("Mabani")

Teacher1 = Teacher("Shohreh" , "Kazemi" , True , "Computer" , "OS")
Teacher2 = Teacher("Arash" , "Paydar" , False , "Computer" , "Mabani")

Teacher1.SetScore(Student1 , 18.5)
Teacher2.SetScore(Student1 , 20)
Teacher2.SetScore(Student2 , 10)

print(Student1.Scores)
print(Student1.ShowAVG())

print(Student.Info)