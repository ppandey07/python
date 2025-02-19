# 08 WAP to ask to user to enter names of their 3 favorite movies & store them in a lis
# movies_lst = []
# print("enter the name of three fav movies :")
# for i in range (0,3):
#     print("movie_",i+1,": ")
#     movies_lst.append(input())
# print(movies_lst)



#09 WAP to check if alist contains a palindrome of elements
list_1 =['M','A','L','A','Y','A','L','A','M']
list_2 = list_1.copy()
list_2.reverse()
if(list_1 == list_2):
 print("the list is  palindrome")
else:
    print("The provided list is not palindrome")
 
#10 WAP to count the number of students with the "A grade in the following tuple"
grades= ('C','D','A','A','B','B','A')
print(grades.count("A"))
#Store the above values in the list and sort them from A to D
grade_list = ['C','D','A','A','B','B','A']
grade_list.sort()
print(grade_list)
 
  