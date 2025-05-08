password = input("Enter your password: ")

num_of_chars = len(password)

if num_of_chars < 6:
    print("Your password is Weak.")
elif 6 <= num_of_chars <= 10:
    print("Your password is Medium.")
elif num_of_chars > 10:
    print("Your password is Strong.")