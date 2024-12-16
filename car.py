class Car :
    def __init__(self , company , model , year):
        self.company = company
        self.model = model
        self.year = year

benz = Car("Mercedes Benz" , "C200" , 2010)
pride = Car("Saipa" , "Pride" , 2000)
print(benz.year)
print(pride.year)