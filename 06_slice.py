#slicing negative index concept
str = 'apple'
#    -5-4-3-2-1
print(str[:-1]) #same concept as positive

#string function
#1. endswith
exam_1 = 'i am huustler'
print(exam_1.endswith('r'))

#2. capitalize
print(exam_1.capitalize())#convert to captial only first character by creating new string

#3. replace 
print(exam_1.replace("am","is")) # old_value ---> new_value

#4. find 
print(exam_1.find("am")) #return the first index of the word or -1

#5. count
print(exam_1.count('u')) # return the count of the given char or string


