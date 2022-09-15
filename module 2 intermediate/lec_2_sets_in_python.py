'''
create a function unique , that takes in a list and returns only unique value or items
unique(["ruby","ruby","python"])
'''

def unique(language):
    return set(language)

print(unique(["ruby","ruby","python"]))