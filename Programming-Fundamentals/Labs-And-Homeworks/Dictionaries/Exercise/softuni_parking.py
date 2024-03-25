number_of_commands = int(input())
parking_lot = {}

for _ in range(number_of_commands):
    command, username, *args = input().split()

    if command == "register":
        license_plate = args[0]
        if username in parking_lot:
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            parking_lot[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
    elif command == "unregister":
        if username not in parking_lot:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")

for username, license_plate in parking_lot.items():
    print(f"{username} => {license_plate}")