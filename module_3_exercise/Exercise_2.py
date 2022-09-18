'''
-----------> loops & lists<-----------------
declare a function which given an list and return the sum of the numbers

'''

def sum_list(numbers):
    count = 0
    for number in numbers:
        count += number
    
    return count

print( sum_list([1,2,3]))


'''
find max number in the lists of numbers:
'''

def find_max(numbers):
    current_max = numbers[0]

    for number in numbers:
        if number > current_max:
            current_max = number
    return current_max

print(find_max([1,5,9,11,17,5,48,6,3,2,10]))
