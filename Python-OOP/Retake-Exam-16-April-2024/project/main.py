from project.sphere_restaurant_app import SphereRestaurantApp

sphere_restaurant_app = SphereRestaurantApp()

print(sphere_restaurant_app.hire_waiter("FullTimeWaiter", "John", 40))
print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Alice", 20))
print(sphere_restaurant_app.hire_waiter("InvalidWaiter", "JohnDoe", 10))
print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Charlie", 30))
print(sphere_restaurant_app.hire_waiter("FullTimeWaiter", "Frank", 50))
print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Alice", 60))

print(sphere_restaurant_app.admit_client("InvalidClient", "JohnDoe"))
print(sphere_restaurant_app.admit_client("VIPClient", "Eve"))
print(sphere_restaurant_app.admit_client("VIPClient", "Lila"))
print(sphere_restaurant_app.admit_client("RegularClient", "Bob"))
print(sphere_restaurant_app.admit_client("VIPClient", "Eve"))
print(sphere_restaurant_app.admit_client("RegularClient", "Oscar"))

print(sphere_restaurant_app.process_shifts("John"))
print(sphere_restaurant_app.process_shifts("Alice"))
print(sphere_restaurant_app.process_shifts("Emily"))
print(sphere_restaurant_app.process_shifts("Frank"))

print(sphere_restaurant_app.process_client_order("Bob", 100.0))
print(sphere_restaurant_app.process_client_order("Eve", 500.0))
print(sphere_restaurant_app.process_client_order("JohnDoe", 250.0))
print(sphere_restaurant_app.process_client_order("Bob", 750.0))
print(sphere_restaurant_app.process_client_order("Lila", 550.0))
print(sphere_restaurant_app.process_client_order("Oscar", 84.0))

print(sphere_restaurant_app.apply_discount_to_client("Lila"))
print(sphere_restaurant_app.apply_discount_to_client("Eve"))
print(sphere_restaurant_app.apply_discount_to_client("JohnDoe"))
print(sphere_restaurant_app.apply_discount_to_client("Oscar"))
print(sphere_restaurant_app.apply_discount_to_client("Bob"))

print(sphere_restaurant_app.generate_report())