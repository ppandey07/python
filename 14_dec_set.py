# dictionary is the data structure that stores key value pair
#points to be remembered during the creation of dict
# no duplicate keys are allowed 
#dict is mutuable
#keys for the dict can be --> int,float,boolean,tuples,strings becoz this things are immutable 
info ={
    'key':'value',
    'name':'apnacollege',
    'learning':'coding',
    'age': 21,
    'is_adult' : True,
    'subjects' :['python','spcc','toc'],
    'topics': ('dictionary','sets')
}
print(info,type(info))
print(info['name'])
print(info['learning'])
print(info['is_adult'])
print(info['subjects'])
print(info['topics'])
print(info['key'])
print(info['age'])

#adding and updating the new values
info['name'] = 'prasad' # it will overwrite rather than creating new key
info['surname'] ='pandey'
print(info)

null_dict ={} #null dictionary can be created

dict ={
    'name': 'prasad',
    'cgpa': 9.6,
    'marks':[92,45,67]
}
print(dict['marks'][0])

#nested dictionary
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
print(student)
print(student['subjects_marks']['java'])
