#OOPS concept is used to increase the reusability and map with real world scenario

# for creation of object there is the need of class
class student: # class name as student
    Name = "arjun"

s1 = student() # creating instance of the class / object
s2 =student()
print(s1)
print(s1.Name)
print(s2)

#class 2
class car:
    color ="blue"
    brand= 'jagur'
    fuel_type = 'cng and petrol'
    fleet ='SUV'

c1= car()
print(c1.color)

# init function is the constructor that get automatically invoke when class is being initiated
# the self parameter is a referecne to the current instance of the class and is used to access variables that belongs to the class

# types of constructor
#1.default constructor
#2. parameterized constructor
class event :
    name_event = 'RGIT tech fest'
    def __init__(self): #default constructor
        pass
    def __init__(self,fullname,date,cost): #parameterized consturctor
        self.name = fullname # self can be written has any name
        self.date = date
        self.cost = cost
        print(self) # this object is same as e1 
        print("This year event will be on the grand scale")

e1 =event("Jayesh",27,132003)
print(e1.name,e1.date)

e2 = event("ramesh",23,43)
print(e2.name,e2.cost)


