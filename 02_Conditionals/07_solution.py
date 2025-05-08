order_size=input("Enter the order size: ")
extra_shot=input("Do you want an extra shot? (yes/no): ")

if order_size == "small":
    if extra_shot == "yes":
        print("Your order is a small coffee with an extra shot.")
    else:
        print("Your order is a small coffee without an extra shot.")
elif order_size == "medium":
    if extra_shot == "yes":
        print("Your order is a medium coffee with an extra shot.")
    else:
        print("Your order is a medium coffee without an extra shot.")
elif order_size == "large":
    if extra_shot == "yes":
        print("Your order is a large coffee with an extra shot.")
    else:
        print("Your order is a large coffee without an extra shot.")
else:
    print("Invalid order size. Please enter small, medium, or large.")