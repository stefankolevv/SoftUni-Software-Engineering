function deleteByEmail() {
    const searchStr = document.querySelector('input[name="email"]').value.toLowerCase();
    const people = document.querySelectorAll('table tbody tr td:nth-child(2)');
    const resultEl = document.querySelector('#result');

    if (searchStr == '') return;
    
    people.forEach(person => {
        if (person.textContent.toLowerCase().includes(searchStr)) {
            person.parentElement.remove();
            resultEl.textContent = 'Deleted.';
        } else {
            resultEl.textContent = 'Not found.';
        }
    });
}