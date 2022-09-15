fruits = ["🍎","🍌","🍓","👶","🍪"]

# use for loop ****

for fruit in fruits:
    print("fruit:", fruit)


print(list(enumerate(fruits)))

# here list takes different data structure or data types and enumerate function take array ans return the index position and the value of index....

# add some 

fruits.append("🍎")


# add with the help of range function or method:

for _ in range(10):
    # print(fruits)
    fruits.append("🍎")
    
