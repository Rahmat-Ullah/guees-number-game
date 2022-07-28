secret_number = 7

user_number = int(input("Enter a number between 0 to 10: "))

while user_number != secret_number:
    print("Oops!, Your guess is not correct.")
    user_number = int(input("Enter a number between 0 to 10 again: "))
print("Your guess is correct, You are free now.")
