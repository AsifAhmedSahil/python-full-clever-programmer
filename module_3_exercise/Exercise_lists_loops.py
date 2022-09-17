'''
double the list ****

step1: create empty list
step2: loop through abd append the list
step3: return that list
'''

from ctypes.wintypes import PINT
from unittest import result


def double(numbers: list)->list:
    result = []
    for number in numbers:
        result.append(number * 2)
    return result

doubleList = double([1,3,5])
print(doubleList)

'''
count word if given a string 
should count & return  the number of words

here split method break it split it and return and list then len check list length***
'''
def count_word(phrase): return len(phrase.split())

print(count_word('hi my name is sahil'))


'''
create a function that given a list of numbers it can return their sum****

'''

def sum_list(numbers):
    count = 0

    for number in numbers:
        count += number
    
    return count

print(sum_list([1,2,3]))