function solve() {

    const input = Number(document.querySelector('#input').value);
    const convertTo = document.querySelector('#selectMenuTo').value.toLowerCase();
    const resultEl = document.querySelector('#result');

    switch (convertTo) {
        case 'binary':
            resultEl.value = input.toString(2);
            break;
        case 'hexadecimal':
            resultEl.value = input.toString(16).toUpperCase();
            break;
    }

}