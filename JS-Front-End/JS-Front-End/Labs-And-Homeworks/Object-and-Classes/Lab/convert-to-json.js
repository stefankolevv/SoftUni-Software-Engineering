function solve(firstName, lastName, hairColor) {
    let person = { name: firstName, lastName, hairColor };
    console.log(JSON.stringify(person));
}

// Test Case

solve('George', 'Jones', 'Brown');
solve('Peter', 'Smith', 'Blond');