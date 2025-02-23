#list traversing
list = [1,2,3]
for item in list:
    print(item)

veg = ['potato','brijal','ladyfinger','cucumber']
for bhaji in veg:
    print(bhaji)

#tuple traversing
tup = (1,2,3,4,5,67,8,9)
for t in tup:
    print(t)

#string traversing
str = "mera college"
for char in str:
    print(char)
# In python with for loops we can use else condition to print any last value once the loop has been ended

for i in range(1,6):
    print(i**i)
else:
    print('khatma tata bye bye')

sen = "prasadpandey"
for char in sen:
    if(char=='e'):
        print('e found')
        break
    print(char)
else:
    print('end')# here this has not been executed because loop has not completetly executed