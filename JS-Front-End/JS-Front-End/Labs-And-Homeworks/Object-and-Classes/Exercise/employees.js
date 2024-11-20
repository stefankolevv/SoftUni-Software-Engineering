function solve(input) {

    function processEmployees(list) {
        return list.reduce((employees, person) => {
            employees[person] = person.length
            return employees;
        },{});
    }

    function printEmployees(employees) {
        for (const employee in employees) {
            console.log(`Name: ${employee} -- Personal Number: ${employees[employee]}`);
        }
    }

    printEmployees(processEmployees(input));
}

// Test Case

solve(['Silas Butler', 'Adnaan Buckley', 'Juan Peterson', 'Brendan Villarreal']);
solve(['Samuel Jackson', 'Will Smith', 'Bruce Willis', 'Tom Holland']);