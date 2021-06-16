'''
Author: RahulV
Cr.Date: 2021-05-31
'''

students = {} #one way to declare a dictionary
students = dict()
students = {
            1: 'A',
            2: 'B',
            3: 'C',
            -1: 'Z'
           }

#fet value by key
value1 = students[1]
value2 = students.get(2)

#Let add 'D' in the list
students[4] = [1,2,3]
students[5] = {'aa': 1,
               'dd': 2
               }
       #Key   #Value
l = [1,2,3]
students[l] = 'some value'
l.append(5)

print(students[l])

for key in students:
    value = students.get(key)
    print(value)

print('----------------')

print(students.items())
for key,value in students.items():
    print(key, value)