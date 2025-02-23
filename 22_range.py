#range (start?,stop,steps?) --> ? denote the optional
print(range(5)) # it will print range 
seq = range(5)
print(seq)#same output

# to print each number we have iterate
for i in seq:
    print(i)
    #or
for i in range(25):#stop
    print(i)

for i in range(2,20):# start and stop
    print(i)
for i in range(2,20,2):#start stop and step
    print(i)