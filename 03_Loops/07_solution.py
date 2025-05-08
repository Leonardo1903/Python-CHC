number=int(input("Enter a number between 1 and 10: "))

while True:
    if number < 1 or number > 10:
        print("Invalid input. Please enter a number between 1 and 10.")
        number = int(input("Enter a number between 1 and 10: "))
    else:
        break
    
