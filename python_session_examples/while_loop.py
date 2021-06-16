'''
Author:
Example: while, break, continue
'''

x = [1,2,3,4,5]
index = 0
while True:
    val = x[index]
    index += 1
    if val == 3:
        continue

    print(val)
    if index == 2:
        break;

print('some statement.')