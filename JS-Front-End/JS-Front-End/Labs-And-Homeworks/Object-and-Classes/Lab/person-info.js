function personInfo(firstName, lastName, age) {
    let person = {
        firstName: firstName,
        lastName: lastName,
        age: age
    };
    return person;
}

// Test Case

console.log(personInfo("Peter", "Pan", "20"));
console.log(personInfo("George", "Smith", "18"));