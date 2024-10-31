function calculator(num1, operator, num2) {
    
    let result;
    switch (operator) {
        case '+': 
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            result = num1 / num2;
             break;
    }

    console.log(result.toFixed(2));
}


// Test Case

calculator(5, '+', 10);
calculator(25.5, '-', 3);