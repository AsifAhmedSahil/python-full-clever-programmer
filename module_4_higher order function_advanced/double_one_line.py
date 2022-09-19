# one line double functions with lambda **

print(list(map(lambda num : num * 2,[1,3,6])))
    

# one line square functions with lambda **

print(list(map(lambda num : num ** 2,[1,3,6])))

# even number generator in a list with lambda function

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(list(filter(lambda number : number % 2 == 0,numbers)))
