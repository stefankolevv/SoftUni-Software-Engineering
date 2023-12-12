import re

def validate_data(password, username):
    if not re.search(r'[A-Z]', password):
        return "Please add a uppercase."

    if not re.search(r'[!@#$%^&*()_]', password):
        return "For better security add a special character."

    if not re.search(r'[123456789]', password):
        return "Add a number to your password."

    if len(password) < 8:
        return "Create a longer password."

    if len(password) > 14:
        return "Create a shorter password."

    if len(username) < 3:
        return "Your username should be at least 3 characters."

    return "Welcome!"

print("Login / Register \n--------------------------")

username = input("Username:")
password = input("Password:")

print("--------------------------")
print(validate_data(password, username))
