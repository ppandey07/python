'''
abstraction - hidding the unnecessary info form the user
encapsultion - create capsule of data and related function ---> we are using this feature from the starting
'''
class car :
    def __init__(self):
        self.acc =False
        self.brk =False
        self.clutch =False

    def start(self):
        self.clutch =True #hidden
        self.acc =True # hidden
        print("Car started")

car_1 = car()
car_1.start()



