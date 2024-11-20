function makeADictionary(arr) {
    const dictionary = arr.reduce((dict, json) => {
        const entry = JSON.parse(json);
        return { ...dict, ...entry };
    }, {});

    Object.entries(dictionary)
        .sort(([a], [b]) => a.localeCompare(b))
        .forEach(([term, definition]) => console.log(`Term: ${term} => Definition: ${definition}`));
}
