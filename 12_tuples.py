tup = {2,4,6,8,10}

print(tup) # tuples are immuatable it means once created cannot be change in the original
# tup[3]=7 --> invalid statement

# advice to store single value in the tuple 

single_value = (3,)#if this is not done then the python will interpretet has the intger value rather than tuple
deve = ("choti","moti","loti","hoti")
print(deve[0])

#slicing concept is same as string and list in tuple
print(deve[1:len(deve)])

#methods in tuple
#1. index-return the index of the firstly occurence of the element
temp_tup = (1,2,3,2,4,5)
print(temp_tup.index(2))

#2. count
print(temp_tup.count(2))