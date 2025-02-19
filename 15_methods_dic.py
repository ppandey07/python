student ={
    'name':'apnacollege',
    'learning':'coding',
    'age': 21,
    'is_adult' : True,

    'subjects_marks' :{
        'python':23,
        'java':45,            # ----> nested dictionary
        'html':54
    },
    'topics': ('dictionary','sets')

}
# keys
print(student.keys())
print(student['subjects_marks'].keys())
print(list(student.keys())) # type casting in the list
print(len(student)) # to find out no. of key value pair in dict
print(len(list(student.keys()))) # another method for the same

# values
print(student.values())
print(list(student.values()))

#items
print(student.items()) # return key value pair in the form of tuples
pair = list(student.items())
print(pair[0]) # items in the dictionary can be accessed like this

#get -return the value of the given key
print(student['name'])# it will directly give error if key is not found
print(student.get('name')) # it will return the none value so it is for preferable for the stability of the system

#update
student.update({'city':'mumbai'})
print(student)

new_dict = {'age': 25}
student.update(new_dict)#another way if the same key is passed then it will overwrite
print(student)
