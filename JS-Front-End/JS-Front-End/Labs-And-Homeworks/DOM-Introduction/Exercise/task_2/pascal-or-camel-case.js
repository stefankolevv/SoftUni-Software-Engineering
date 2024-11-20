function solve() {

    const input = document.querySelector('#text').value.toLowerCase().split(' ');
    const convention = document.querySelector('#naming-convention').value.toLowerCase().trim();

    const resultEl = document.querySelector('#result');

    function capitaliseWord(word) {
        return word[0].toUpperCase() + word.slice(1);
    }

    switch (convention) {
        case 'camel case':
            resultEl.textContent = input[0] + input.slice(1).map(capitaliseWord).join('');
            break;
        case 'pascal case':
            resultEl.textContent = input.map(capitaliseWord).join('');
            break;
        default:
            resultEl.textContent = 'Error!';
    }
}