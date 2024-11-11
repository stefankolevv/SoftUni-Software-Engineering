function calculate(x, y, operator) {

    const operations = [];
    
    operations['multiply'] = (a, b) => a * b;
    operations['divide'] = (a, b) => a / b;
    operations['add'] = (a, b) => a + b;
    operations['subtract'] = (a, b) => a - b;

    console.log(operations[operator](x, y));
}

// Test Case

calculate(5, 5, 'multiply');
calculate(40, 8, 'divide');
calculate(12, 19, 'add');
calculate(50, 13, 'subtract');