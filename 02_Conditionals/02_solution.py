age=int(input("Enter your age: "))
day=input("Enter the day of the week: ")

price=12 if age>=18 else 8

if day == "Wednesday":
    price -= 2
    
print(f"The ticket price is: ${price}")

