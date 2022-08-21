class Car:

    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This " + self.make + " is driving")
        print(self.model +" !")

    def stop(self):
        print("This " + self.make + " is stopped")
