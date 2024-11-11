function findHashtags(input) {
    const hashtags = input.match(/#\w+/g);
    const validWords = hashtags ? hashtags
        .map(tag => tag.substring(1))
        .filter(word => /^[a-zA-Z]+$/.test(word)) : [];
    validWords.forEach(word => console.log(word));
}

// Test Case

findHashtags('Nowadays everyone uses # to tag a #special word in #socialMedia');
findHashtags('The symbol # is known #variously in English-speaking #regions as the #number sign');