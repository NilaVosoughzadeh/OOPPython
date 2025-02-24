#Class - First Word Capitalize

class MyClass :
    def __init__(self):
        self.name = "nila"
        self.lastName = "Vo"

object1 = MyClass()
print(object1.name , object1.lastName)


class HerClass :
    def __init__(self , name , lastname):
        self.myname = name
        self.mylastName = lastname

    def fullname(self) :
        print("Hello honey")

object2 = HerClass("nima" , "vivo")
print(object2.myname , object2.mylastName)
print(object2.fullname())