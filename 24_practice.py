# 22 WAP to find the sum of first n numbers using while loop
n =int(input('enter the num:'))
sum=0
while (n!=0):
    sum =sum+n
    n-=1
print(sum)
#23. WAP to find the factorial of first n numbers using for loop
f =int(input('enter the num:'))
fact=1
for i in range(1,f+1):
    fact =fact*i
print(fact)