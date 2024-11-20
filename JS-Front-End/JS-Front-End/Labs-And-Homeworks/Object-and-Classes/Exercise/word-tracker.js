function wordTracker(arr) {
    const [wordsToTrack, ...words] = arr;
    const tracker = Object.fromEntries(wordsToTrack.split(' ').map(word => [word, 0]));

    words.forEach(word => {
        if (tracker.hasOwnProperty(word)) {
            tracker[word]++;
        }
    });

    Object.entries(tracker)
        .sort((a, b) => b[1] - a[1])
        .forEach(([word, count]) => console.log(`${word} - ${count}`));
}
