username = input()
user_password = input()
current_password = input()

while user_password != current_password:
    current_password = input()

print(f"Welcome {username}!")