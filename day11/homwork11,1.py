"""რიცხვის გამოცნობა: დაწერეთ პროგრამა,
რომელიც სთხოვს მომხმარებელს გამოიცნოს რიცხვი (მაგ., 5, ეს რიცხვი თქვენ აირჩიეთ). 
განაგრძეთ კითხვა, სანამ არ გამოიცნობენ სწორად."""

number = float(input("Please enter a number from 1 to 10:"))

i = 5

while i <= 10:
    if number == 5:
        print("You won")
    else:
        print("You lost,  Please try again")







