function addItem() {
    
    const inputEl = document.querySelector('#newItemText');
    const listEl = document.querySelector('#items');

    if (inputEl.value == '') return;

    const newListItem = document.createElement('li');

    newListItem.textContent = inputEl.value;

    listEl.appendChild(newListItem);

    inputEl.value = '';
}
