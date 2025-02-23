# function are used to reduce the redundancy of the same block of code 
#function defination
def cal_sum(a,b):# parametrs
    sum = a+b
    print(sum)

cal_sum(10,11)
cal_sum(4,12)
cal_sum(34,78) #function call as arguments

# function without parametrs and return value is also possible 
def print_hello():
    print('hello')
print_hello()

# cal avg of three numbers
def avg(a,b,c):
    avg = (a+b+c)/3
    print(int(avg))

avg(1,2,3)
#to print two differnet values next to others then use end =' '
print('prasad',end=' ')
print('deep')

#default values in the parametrs
#default values should be after non default values
def cal_prod(a=2,b=3):
    print(a*b)

cal_prod()
cal_prod(4,5)
cal_prod(5)
