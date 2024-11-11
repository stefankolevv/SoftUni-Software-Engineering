function modifyNumber(num) {
    num = num.toString();
    let average = digitsAverage(num);
    while (average <= 5) {
        num += '9';
        average = digitsAverage(num);
    }
    console.log(num);

    function digitsAverage(num) {
        return num.split('').map(Number).reduce((a, b) => a + b, 0) / num.length;
    }
}

// Test Case

modifyNumber(101);
modifyNumber(5835);