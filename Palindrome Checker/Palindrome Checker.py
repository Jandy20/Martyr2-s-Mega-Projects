user_input = input("Input:").lower()

if user_input == "".join(reversed(user_input)):
    print(user_input+" is a palindrome.")
else:
    print(user_input+" is not a palindrome.")

