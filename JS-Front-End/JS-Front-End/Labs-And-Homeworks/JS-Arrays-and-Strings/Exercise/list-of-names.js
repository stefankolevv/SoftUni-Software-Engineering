function solve(array) {
    array
        .sort((a, b) => a.localeCompare(b))
        .forEach(function(element, index) {
            console.log(`${index + 1}.${element}`);
        });
}

// Test Case

solve(["John", "Bob", "Christina", "Ema"]);