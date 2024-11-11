function solve(array, step) {

    const newArr = [];

    array.forEach(function(el, index) {
        if (index % step === 0) newArr.push(array[index])
    });

    return newArr;
}

// Test Case

console.log(solve([51, 47, 32, 61, 21], 2));
console.log(solve([32, 21, 61, 1], 4));
console.log(solve([2, 4, 15, 31], 5));