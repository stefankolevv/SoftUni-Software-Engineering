function solve() {
    
    const inputEl = document.querySelector('#input');
    const outputEl = document.querySelector('#output');

    const sentences = inputEl.value.split('. ');
    const sentPerPar = 3;

    const numberOfParagraphs = Math.ceil(sentences.length / sentPerPar);

    let output = '';

    for( let i = 0; i < numberOfParagraphs; i++) {
        const start = i * sentPerPar;
        const end = start + sentPerPar;

        output += '<p>';
        output += sentences.slice(start, end).join('. ');
        output += '</p>';
    }

    outputEl.innerHTML = output; 
}