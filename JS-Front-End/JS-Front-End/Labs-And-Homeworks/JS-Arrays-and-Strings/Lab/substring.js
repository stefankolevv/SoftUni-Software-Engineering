function solve(string, startIndex, count) {
    let result = string.substring(startIndex, startIndex + count);
    console.log(result);
}

// Test Case

solve('ASentence', 1, 8);
solve('SkipWord', 4, 7);