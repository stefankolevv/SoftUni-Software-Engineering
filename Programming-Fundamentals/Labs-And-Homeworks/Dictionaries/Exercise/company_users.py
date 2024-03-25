companies = {}

while True:
    command = input()
    if command == "End":
        break

    company, employee_id = command.split(" -> ")

    if company not in companies:
        companies[company] = set()

    companies[company].add(employee_id)

for company, employees in companies.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")

