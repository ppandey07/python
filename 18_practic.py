# 11 store the following word meaning in a python dictionary :
meanings = {
    "table" : ("a piece of furniture","list of facts and figures"),
    "cat" : ("small animal")
}

classrooms = {'python','java','C++','javascript','java','C'}
print(len(classrooms))

# 12 WAP to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary and add one by one .use subject name as key and marks as value.
marks_dic = {}
marks_dic['java'] = int(input('enter the marks of the subject 1: '))
marks_dic['python'] = int(input('enter the marks of the subject 2: '))
marks_dic['toc'] = int(input('enter the marks of the subject 3: '))
print(marks_dic)

# 13 figure out the way to store 9 and 9.0 as separte values in the set
val = {(9,9.0)}
print(val)
# another sol :

val_1 = {('float',9.0),('int',9)}
print(val_1)