# 18  print the elements of the following list using loop
list =[1,4,9,16,25,36,49,65,81,100]
for i in list:
    print(i)

#19 search for a number x in the tuple using for loop

tup =(1,4,9,16,25,36,49,65,81,100)
x = int(input('enter the number to be searched :'))
for i in tup:
    if(x==i):
     print('element found')
     break
else:
   print('not found')

