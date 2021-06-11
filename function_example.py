'''
Author:
'''

def my_function():
    pass

def myFunction():
    pass

def _my_function():
    pass

    #name    #arguments
def addition(amount_1, amount_2=500):
    #body
    sum = amount_1 + amount_2
    avg = 44
    return sum, avg

sum_of_two_value = addition(5, 6)
print(sum_of_two_value[0])

sum_of_two_value = addition(5.6, 6)
print(sum_of_two_value[0])

sum_of_two_value = addition(5.5, 6.5)
print(sum_of_two_value)

sum_of_two_value = addition(5.5)
print(sum_of_two_value)


