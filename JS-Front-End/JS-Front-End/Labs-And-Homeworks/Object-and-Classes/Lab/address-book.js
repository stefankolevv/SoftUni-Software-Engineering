function addressBook(input) {
    let book = {};
    input.forEach(entry => {
        let [name, address] = entry.split(':');
        book[name] = address;
    });
    Object.keys(book).sort().forEach(name => {
        console.log(`${name} -> ${book[name]}`);
    });
}

// Test Case

addressBook(['Tim:Doe Crossing', 'Bill:Nelson Place', 'Peter:Carlyle Ave', 'Bill:Ornery Rd']);
addressBook(['Bob:Huxley Rd', 'John:Milwaukee Crossing', 'Peter:Fordem Ave', 'Bob:Redwing Ave', 'George:Mesta Crossing', 'Ted:Gateway Way', 'Bill:Gateway Way', 'John:Grover Rd', 'Peter:Huxley Rd', 'Jeff:Gateway Way', 'Jeff:Huxley Rd']);