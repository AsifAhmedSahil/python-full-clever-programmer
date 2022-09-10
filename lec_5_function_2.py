'''
take 2 integers and return their sum 
'''

def sum(a,b):
    return a+b

print(sum(3,5))

'''
convert ood calculator using functions
'''

def calculateFoodTotal(food , tip):
    tipAmount = food * (tip / 100)
    total = food + tipAmount
    return total
    

total = calculateFoodTotal(100,10)
print(total)

'''
calculate weather app using function
'''

def weather_function(weather):

    if weather == "rain":
        print("its raining") 
    elif weather == "wind":
        print("its cloudy")
    else:
        print("sunny sunny baby")
weather_function("rain")