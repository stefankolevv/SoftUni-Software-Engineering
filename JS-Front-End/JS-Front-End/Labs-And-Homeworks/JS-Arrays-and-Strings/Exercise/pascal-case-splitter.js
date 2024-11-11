function splitPascalCase(input) {
    const words = input.match(/[A-Z][a-z]*/g);
    console.log(words.join(', '));
}

// Test Case

splitPascalCase('SplitMeIfYouCanHaHaYouCantOrYouCan');
splitPascalCase('HoldTheDoor');
splitPascalCase('ThisIsSoAnnoyingToDo');