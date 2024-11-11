function chechForPalindrones(numbers) {

    const isPalindrome = (num) => {
        const strNum = num.toString();
        const strNumReversed = strNum.split('').reverse().join('');

        return strNum === strNumReversed;
    }

    numbers.forEach(num => console.log(isPalindrome(num)));
}

// Test Case

chechForPalindrones([123,323,421,121]);
chechForPalindrones([32,2,232,1010]);