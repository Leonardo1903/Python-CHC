number=int(input("Enter a number: "))
factorial=1

while number>0:
    factorial*=number
    number-=1

print(f"The factorial is: {factorial}")