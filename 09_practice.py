#07 wap to check odd or even
num = int(input('enter the number : '))
if(num%2==0):
    print("Even")
else:
    print("Odd")
#08 wap to find the greatest of 3 numbers entered by the user
n1 =int(input('enter the first number: '))
n2 =int(input('enter the second number: '))
n3 =int(input('enter the third number: '))
temp=None

if(n1>n2):
    if(n1>n3):
        temp = n1
    else:
        temp =n3
else:
    if(n2>n3):
        temp = n2
    else:
        temp = n3

print("The largest number among ",n1,n2,n3," is ",temp)