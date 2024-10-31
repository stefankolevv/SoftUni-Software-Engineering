function solve(num) {
    const stringFromNumber = num.toString();

    let sum = 0;
    for (let i = 0; i < stringFromNumber.length; i++) {
        sum += Number(stringFromNumber[i]);
    }

    console.log(sum);
}

// Test Case

solve(245678);
solve(97561);
solve(543);