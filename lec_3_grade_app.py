grade = int(input("whats your marks? : "))

if 60 <= grade <= 100: #Pythonic style 🙂 
    print("passing grade")

if grade >= 90 :
    print("Congratulations! Your grade is A")
elif grade >= 80:
    print("Your grade is B")
elif grade >= 70:
    print("Your grade is C")
elif grade >= 60:
    print("Your grade is D")
else:
    print("Your grade is F. You Failed!")