function checkSign(num1, num2, num3) {

    const array = [num1, num2, num3];

    const isNegative = array.filter(num => num < 0).length % 2 !== 0;

    console.log(isNegative ? 'Negative' : 'Positive');
}

// Test Case

checkSign(5, 12, -15);
checkSign(-6, -12, 14);