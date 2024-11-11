function solve(text, word) {

    function repeat(word) {
        return '*'.repeat(word.length);  
    }

    let censored = text.replace(word, repeat(word));
    while (censored.includes(word))
        censored = censored.replace(word, repeat(word));
    
    console.log(censored);
}

// Test Case

solve('A small sentence with some words', 'small');
solve('Find the hidden word', 'hidden');