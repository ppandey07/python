# arithemic operators
a = 17
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b) # always return floating no matter whether it is intger or float
print(a%b)
print(a**b) # a^b

# realtional operator

c =10
d =4


print(c==d)
print(c!=d)
print(c>=d)
print(c<=d)
print(c>d)
print(c<d)

# assignment operator
num = 10
num **=5 # num = num**5
print(num)

#logical operators
n1 = False
n2 = False
print(not n1)
print("and opertor answer:",n1 and n2)
print("or operator answer :",n1 or n2)

c =1 
d = 3  
print(c and d) # first falsy or last truthy value are returned by and operator in case of integer
print(c or d) # first truthy or last falsy value are returned by or operator in case of integer

#conversion : interpreter automatically do it for us
m = 40
n= 30.6
print(m+n) # here integer m is automatically converted to float value 

#type casting : forcefully we convert it
o ='3'
p = 5
print(int(o)+p) # here we are forcefully converted the string into integer using int() function
st = str(3.14) # similarly it converted to string using string function
print(type(st))

