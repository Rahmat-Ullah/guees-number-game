secret_number = 7

user_number = int(input("Enter the number: "))

while user_number != secret_number:
    print("Oops!, Your guess is not correct.")
    user_number = int(input("Enter the number again: "))
print("Your guess is correct, You are free now.")