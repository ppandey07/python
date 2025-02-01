var_1 = input("enter your name  : ") #input function always take string input means it convert the given input into string type
print(type(var_1),var_1) 
#so to take different datatypes input we need
var_2 =int(input("enter your age :"))
print(type(var_2,),var_2)

var_2 =float(input("enter your age :"))
print(type(var_2,),var_2)

var_2 =bool(input("enter your age :"))
print(type(var_2,),var_2) # only empty string will return the false otherwise true for all input