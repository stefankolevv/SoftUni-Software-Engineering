function wordsUppercase(text) {
    const words = text.match(/\w+/g).map(word => word.toUpperCase());
    console.log(words.join(', '));
}

// Test Case

wordsUppercase('Hi, how are you?');
wordsUppercase('hello');