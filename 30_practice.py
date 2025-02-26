# 30 create student class that take name and marks of 3 sub as argument in constructor then create a method to print the average
class student:
    def __init__(self,name,sub_1,sub_2,sub_3):
        self.name =name
        self.sub_1 = sub_1
        self.sub_2 = sub_2
        self.sub_3 = sub_3
    def avg(self):
      sum = self.sub_1+self.sub_2+self.sub_3
      return sum /3
    
s1 = student('raj',32,56,92)
print('the avg of three subject of',s1.name,'is',s1.avg())

#other way
class student_2:
    def __init__(self,name,marks):
        self.name =name
        self.marks = marks
    
    def avg(self):
      sum = 0
      for value in self.marks:
         sum = sum + value
      avg = sum / 3
      print('the avg of three subject of',s1.name,'is',avg)

s1 = student_2('raj',[32,56,92])
s1.avg()
