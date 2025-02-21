# Methods :
temp_set = {1,2,3,5,6,7,12}

#1. add 
temp_set.add(34)
print(temp_set)

#2. remove 
temp_set.remove(7)
print(temp_set)

#3. clear 
temp_set.clear()
print(temp_set)

#4.pop
temp_set = {1,2,3,5,6,7,12}
temp_set.pop()
print(temp_set)

# 5. union 
temp_set_2 = {10,11,15,5}

print(temp_set.union(temp_set_2))# here og set has not been changed but it returns the new set 
print(temp_set.intersection(temp_set_2))

