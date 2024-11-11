function oddAndEvenSum(num) {
    const digits = Math.abs(num).toString().split('').map(Number);
    let eSum = 0, oSum = 0;
    digits.forEach(d => (d % 2 == 0) ? eSum += d : oSum += d);
    console.log(`Odd sum = ${oSum}, Even sum = ${eSum}`);
}

// Test Case

oddAndEvenSum(1000435)	 
oddAndEvenSum(3495892137259234);	 