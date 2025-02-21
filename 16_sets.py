#sets - unorded items , mutable
#element in the set is ,unique,immutable
# dict and list can't be stored in the sets because they are mutable

nums ={1,2,3,4,5}
print(nums)
collection = {'hello',1,40.56,(3,4,5),(3,4)}
print(collection)
same_value ={2,2,2,2} # it will ignore the same 
print(same_value)
print(len(same_value)) #length function will also ignore the duplicate values

# creating the empty set
empty_set = set()
print(empty_set)