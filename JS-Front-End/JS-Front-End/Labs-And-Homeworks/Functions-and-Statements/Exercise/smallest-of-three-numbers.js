function findSmallestNumber(num1, num2, num3) {
    return Math.min(...arguments);
}

// Test Case

console.log(findSmallestNumber(2, 5, 3));
console.log(findSmallestNumber(600, 342, 123));
console.log(findSmallestNumber(25, 23, 4));
console.log(findSmallestNumber(2, 2, 2));