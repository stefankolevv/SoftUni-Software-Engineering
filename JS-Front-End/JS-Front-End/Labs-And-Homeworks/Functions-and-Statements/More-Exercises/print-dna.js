function printDNA(length) {
    const sequence = 'ATCGTTAGGG';
    for (let i = 0; i < length; i++) {
        let row = i % 4;
        let symbols = sequence[(i * 2) % sequence.length] + sequence[(i * 2 + 1) % sequence.length];
        if (row === 0) console.log(`**${symbols}**`);
        else if (row === 1 || row === 3) console.log(`*${symbols[0]}--${symbols[1]}*`);
        else if (row === 2) console.log(`${symbols[0]}----${symbols[1]}`);
    }
}

// Test Case

printDNA(4);
printDNA(10);