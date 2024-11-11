function revealWords(words, template) {
    const wordArray = words.split(', ');
    const result = template.split(' ').map(word => {
        if (word.includes('*')) {
            const matchingWord = wordArray.find(w => w.length === word.length);
            return matchingWord || word;
        }
        return word;
    });
    console.log(result.join(' '));
}

// Test Case

revealWords('great', 'softuni is ***** place for learning new programming languages');
revealWords('great, learning', 'softuni is ***** place for ******** new programming languages');