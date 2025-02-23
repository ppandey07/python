#14 print no from 1 to 100
i=1
while (i<=100):
    print(i)
    i+=1
#15.print 100 to 1
j =100
while(j>=1):
    print(j)
    j = j-1
# 16 print the elements of the following list using a loop

list_ =[1,4,9,16,25,36,49,81,100]
i=0
while (i<len(list_)):
    print(list_[i])
    i=i+1
#17 print table for the number n
n =int(input('enter the number :'))
h = 1
while(h<=10):
    print(n,'x',h,'=',n*h)
    h=h+1
tuple = (1,4,9,16,25,36,49,81,100,16)
x = int(input('enter the number to be searched :'))
k=0
flag =0
# while (k<len(tuple)):
#     if(x ==tuple[k]):
#         flag =1
#     k+=1

# if(flag):
#      print("the element is present in the tuple")
# else:
#      print("the element is not present in the tuple")
        
while (k<len(tuple)):
    if(x ==tuple[k]):
        print('Found at index :',k)
    else:
        print('finding.....')
    k+=1

#break
i = 0
while(i<10):
    if(i==9):
        break
    print(i)
    i=i+1

#continue
i=0
while(i<=100):
    if(i%2!=0):
        i=i+1
        continue
    print(i)
    i=i+1

