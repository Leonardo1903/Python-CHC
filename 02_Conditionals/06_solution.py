distance=int(input("Enter the distance in km: "))

if 0<= distance < 3:
    print("You can walk.")
elif 3<= distance < 10:
    print("You can cycle.")
elif 10<= distance < 50:
    print("You can drive.")