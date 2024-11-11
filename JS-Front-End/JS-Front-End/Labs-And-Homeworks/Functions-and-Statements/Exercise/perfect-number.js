function isPerfectNumber(num) {

    let sum = 1;

    for ( let i = 2; i < num; i++) {
        if (num % i === 0) sum += i;
    }

    if (num === sum) {
        console.log('We have a perfect number!');
    } else {
        console.log("It's not so perfect.");
    }
}

// Test Case

isPerfectNumber(6);
isPerfectNumber(28);
isPerfectNumber(1236498);