document.addEventListener('DOMContentLoaded', solve);

function solve() {
    
    const selectEl = document.querySelector('#menu');

    document.querySelector('form').addEventListener('submit', (e) => {
        e.preventDefault();

        const newItemText = e.target.querySelector('#newItemText').value;
        const newItemValue = e.target.querySelector('#newItemValue').value;

        if (newItemText == '' || newItemValue == '') return;
        
        const newItem = document.createElement('option');

        newItem.textContent = newItemText;
        newItem.setAttribute('value', newItemValue);

        selectEl.append(newItem);

        e.target.reset();
        e.target.querySelector('#newItemText').focus();
    });
}