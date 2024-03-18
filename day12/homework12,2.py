number = float(input("Please enter a number from 1 to 10:"))

while number % 2 != 0:
    print("This number Odd")
    break
else:
    print("This number Even")