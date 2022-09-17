# if you can returnn back result as a flote operator value then use "/"
# but you can not want to return float then use "//"

food_amount = float(input('Enter Your Food Amount $: '))
tip_percentage = float(input('Enter Your Tip %: ')) / 100

tip_amount = food_amount * tip_percentage

total = food_amount + tip_amount

print("Total Amount: $" + str(total))

