function solve(num1, num2) {

    let sum = 0;
    let log = '';

    for (let i = num1; i <= num2; i++) {
        log += i + ' ';
        sum += i;
    }

    console.log(log.trim());
    console.log(`Sum: ${sum}`);
}

// Test Case

solve(5, 10);
solve(0, 26);
solve(50, 60);