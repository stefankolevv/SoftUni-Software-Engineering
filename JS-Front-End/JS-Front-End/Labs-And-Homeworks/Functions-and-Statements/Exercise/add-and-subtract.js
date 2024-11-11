function addAndSubtract(num1, num2, num3) {
    
    const sum = (x, y) => x + y;
    const subtract = (x, y) => x - y;

    return subtract(sum(num1, num2), num3);
}

// Test Case

console.log(addAndSubtract(23, 6, 10));
console.log(addAndSubtract(1, 17, 30));
console.log(addAndSubtract(42, 58, 100));