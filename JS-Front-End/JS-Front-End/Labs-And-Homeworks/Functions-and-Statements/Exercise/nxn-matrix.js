function printNumberMatrix(n) {
    const result = ((n + ' ').repeat(n) + '\n').repeat(n);
    console.log(result);
}

// Test Case

printNumberMatrix(5);
printNumberMatrix(9);