#concept of slicing in the list
marks =[10,30,450,50]
print(marks[0:3]) #slicing concept is same as string 

#methods in list 
# 1.append
list = [1,24,5,3,45]
list.append(75) # we cannot do this --> print(list.append(75)) because it returns None value and not as the string it return new string
print(list)
# 2.sort
list.sort()
print(list)
# 3.sort in reverse
list.sort(reverse=True)
print(list) 
# 4.reverse
list.reverse()
print(list)
# 5.insert (indx,val)
list.insert(1,19)
print(list)

#6 remove  first occurrence of the given number
temp_list = [1,4,3,34,3,6]
temp_list.remove(3)
print(temp_list)

#7 pop - delete the value from the given index
temp_list.pop(2)
print(temp_list)
