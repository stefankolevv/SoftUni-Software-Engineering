function solve(jsonStr) {
    let obj = JSON.parse(jsonStr);
    
    for (let key in obj) {
        console.log(`${key}: ${obj[key]}`);
    }
}

// Test Case

solve('{"name": "George", "age": 40, "town": "Sofia"}');
solve('{"name": "Peter", "age": 35, "town": "Plovdiv"}');