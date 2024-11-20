function oddOccurrences(input) {
    const words = input.toLowerCase().split(' ');
    const occurrences = {};

    words.forEach(word => {
        occurrences[word] = (occurrences[word] || 0) + 1;
    });

    console.log(Object.entries(occurrences)
        .filter(([_, count]) => count % 2 !== 0)
        .map(([word]) => word)
        .join(' '));
}
