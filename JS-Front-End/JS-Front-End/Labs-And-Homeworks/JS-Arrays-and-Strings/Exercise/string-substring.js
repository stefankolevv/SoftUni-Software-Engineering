function checkSubstring(word, text) {
    const lowerCaseWord = word.toLowerCase();
    const lowerCaseText = text.toLowerCase();
    
    const regex = new RegExp(`\\b${lowerCaseWord}\\b`);
    
    if (regex.test(lowerCaseText)) {
        console.log(lowerCaseWord);
    } else {
        console.log(`${word} not found!`);
    }
}

// Test Case

checkSubstring('javascript', 'JavaScript is the best programming language');
checkSubstring('python', 'JavaScript is the best programming language');