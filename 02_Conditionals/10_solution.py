pet=input("Enter the type of pet: ")
age=int(input("Enter the age of the pet: "))

if pet == "dog":
    if age<2:
        print("Your pet needs puppy food.")
    else:
        print("Your pet needs adult dog food.")
elif pet == "cat":
    if age>5:
        print("Your pet needs senior cat food.")
    else:
        print("Your pet needs adult cat food.")