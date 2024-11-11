function solve(input) {

    const zippedArray = [];
    const initialArrayLength = input.length;

    input.sort((a, b) => a - b);

    for (let i = 0; i < initialArrayLength; i++) {
        if (i % 2 === 0) {
            const el = input.shift();
            zippedArray.push(el);
        } else {
            const el = input.pop();
            zippedArray.push(el);
        }
    }

    return zippedArray;
}

// Test Case

console.log(solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]));