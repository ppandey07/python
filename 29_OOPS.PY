# attributes
'''
1. class attribute - if all the instance poses same value
2. obj attribute - if all the instance have different value
(more precedence) obj.attr >>> class attr (less precedence)
''' 

class student :
    college = "IIT BOMBAY" # class atr
    name = 'Prasadkumar Pandey' #class attr
    def __init__(self,name):
        self.name = name #obj attr
        print('done')

s1 = student('name change')
print(s1.name) #it will print name change

#data (attribute) - properties --> color,height,weight,size
#methods (performance) - works ---> walk,run,star,stop

class student_2:
    college = "IIT ROORKEE" # class atr
    name = 'anonymous' #class attr
    def __init__(self,name):
        self.name = name #obj attr
        print('done')
    def hello(self):  #methods - similar to function
        print('welcome :',self.name)

s2 = student_2('paa')
s2.hello()