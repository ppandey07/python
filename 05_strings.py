str1='THIS IS the string '
str2="apna college"
str3="""this is also a string"""

# why there are different types of declaration for string
str4= "this is iit's classrooms" #this is the reason if we want to use single asphestrope in the string

#concatination of string
final_str = str1 + str2
print(final_str)

#escape sequence are some special character used to perform certain operation

str = "hello i my name is lucifer.\n i am in 3rd year"
print(str)
str = "hello i my name is lucifer.\t i am in 3rd year"
print(str)

#length function
print(len("hel lo")) # it includes spaces,and other characters

#indexing are used to accessthe particular part of the string
example_1 = "Apun ka college"
print(example_1[0])
print(example_1[1])
print(example_1[2])
print(example_1[3])
print(example_1[4])
print(example_1[5])
print(example_1[6])
print(example_1[7])
# example_1[0] = 'a' # we cannot change the value of og string by this method

#slicing -  used during ml 
exam_2 = "prasad pandey"
print(exam_2[1:5]) # var_name[starting index : end index] end index is not included
print(exam_2[:5]) # assumed start from 0
print(exam_2[0:]) # end is assumed from len(str)

 