function validityChecker(x1, y1, x2, y2) {

    function isValid(x1, y1, x2, y2) {
        const distance = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
        return distance === Math.floor(distance);
    }

    console.log(`{${x1}, ${y1}} to {0, 0} is ${isValid(x1, y1, 0, 0) ? 'valid' : 'invalid'}`);
    console.log(`{${x2}, ${y2}} to {0, 0} is ${isValid(x2, y2, 0, 0) ? 'valid' : 'invalid'}`);
    console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is ${isValid(x1, y1, x2, y2) ? 'valid' : 'invalid'}`);
}


// Test Case

validityChecker(3, 0, 0, 4);
validityChecker(2, 1, 1, 1);