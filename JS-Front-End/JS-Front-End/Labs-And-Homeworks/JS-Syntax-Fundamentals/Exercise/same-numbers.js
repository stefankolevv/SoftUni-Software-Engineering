function solve(num) {

    const stringFromNumber = num.toString();
    let sum = 0;
    let check = true;

    for (let i = 0; i < stringFromNumber.length; i++) {
        if (stringFromNumber[i] !== stringFromNumber[i+1] && i < stringFromNumber.length - 1) {
            check = false;
        }
        sum += Number(stringFromNumber[i]);
    }

    console.log(check);
    console.log(sum);
}

// Test Case

solve(2222222);
solve(1234);