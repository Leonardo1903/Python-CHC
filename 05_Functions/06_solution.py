# Lambda function to calculate the cube of a number
cube = lambda number: number ** 3

number = int(input("Enter a number: "))

print(f"The cube of {number} is {cube(number)}")