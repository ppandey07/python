def show(n):
    if(n==0):
        return 
    print(n)
    show(n-1)

show(5)

#29 write a recursive function to calculate the sum of first n natural numbers
def sum(n):
    if (n==0):
        return 0
    return n+sum(n-1)
print(sum(5))

#write a recursive function to print all elements in a list
def prnt_lst(list,n):
    if(n==len(list)):
        return
    print(list[n])
    prnt_lst(list,n+1)
prnt_lst(["a","b","c"],0)

def prnt_lst_1(list,n):
    if(n==-1):
        return
    prnt_lst_1(list,n-1)
    print(list[n])
prnt_lst_1(["a","b","c"],2)