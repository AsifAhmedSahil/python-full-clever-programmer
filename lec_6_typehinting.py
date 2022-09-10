'''
convert food calculator using functions -----> TYPEHINTING*******

'''

def calculateFoodTotal(food : float , tip: int) -> float:
    tipAmount = food * (tip / 100)
    total = food + tipAmount
    return total
    

total = calculateFoodTotal(100,10)
print(total)