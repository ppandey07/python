#25.WAF to print the length of list (list is the parameter)
def len_list(list):
    length =0
    for i in list:
        length +=1
    print(length)

len_list([1,2,3,4,5])
len_list(["apple","mango","bananna"])

# 26 WAF to print the elements of a list in a single line
def print_list(list):
    for i in list:
     print(i,end=" ")
     
print_list(["apple","mango","bananna"])
#27 WAF to find the factorial of n

def fact(n):
    if(n==0 or n==1):
        return 1
    result = n*fact(n-1)
    return result

print(fact(4))
print(fact(5))

#28 WAF to convert USD to INR
def conver_USD_INR(val):
    res = val*86.59
    return res

print(conver_USD_INR(245))
#WAF that return the string based on the odd or even of the number
def idn_num(num):
    if(num%2==0):
        print("EVEN")
    else:
        print('ODD')
idn_num(45)
idn_num(20)