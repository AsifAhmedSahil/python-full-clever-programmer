# with out using map and filter you can easyly calculate double number and even number also ****
# ===================== only use for loop 

# list
numbers = [1,2,3,4,5,6,7,8,9]

# generate even number using list comprehension

print([number for number in numbers if number % 2 == 0])

# means for loop chalabo then akta number generate krvo then oi number e logic apply krbo ans then oi output k number e save krbo and list return krbo

# double number generator using list comprehension

print([number * 2 for number in numbers ])

# get odd number using list comprehension

print([number for number in numbers if number % 2 != 0])

# get all odd number CUBED ***
print([number ** 3 for number in numbers if number % 2 != 0])