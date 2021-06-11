'''
Author:
'''

class Sample:
    pass

list

persons = ('Sam', 'peter', 'john')

for p in persons:
    print(p)
services = ['email', 'cloud platform']
a = 'Hello, Mr. {0}, this is regarding the service {1}, it will going to be susp...'

s = Sample()
for person in persons:
    for service in services:
        content = a.format(s, service)
        print(content)

