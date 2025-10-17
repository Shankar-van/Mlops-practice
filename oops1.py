#initiate a class
class employee:
    # special method /magic method /dunder method-  constructor
    def __init__(self):
        print("Started Execuring Attriibutes/Data")
        self.id = 1
        self.salary = 50000
        self.designation = "sde"
        print("Attriibutes/Datahave been Initiated")

    def travel(self,destination):
        print("this Traelled function was called Manually")
        print(f"Employee is now travelling to {destination}")

# create an object /instancee of the class 
sam = employee()
# calling a method 
# sam.travel("chennai")

# print(sam.designation)

print(type(sam))
