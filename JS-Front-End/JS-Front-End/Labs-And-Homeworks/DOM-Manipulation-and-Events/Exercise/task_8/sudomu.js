document.addEventListener('DOMContentLoaded', solve);

function solve() {
    
    const formEl = document.querySelector('#solutionCheck');
    const outputEl = document.querySelector('#check');
    const sizeEl = document.querySelector('#size');

    let status = '';
    let size = 3;

    sizeEl.addEventListener('change', (e) => {
        
    });

    formEl.addEventListener('submit', (e) => {
        e.preventDefault();

        const rows = e.target.querySelectorAll('table tbody tr');

        rows.forEach(row => {
            const values = [...row.children].map(el => el.children[0].value);
            const duplicates = values.filter((item, index) => values.indexOf(item) !== index);

            if (duplicates.length > 0) {
                status += '0';
            } else {
                status += '1';
            }            
        });

        status += 'x';

        for (let i = 0; i <= size; i++) {
            const column = e.target.querySelectorAll(`table tbody tr td:nth-child(${i})`)
            const duplicates = column.filter((item, index) => column.indexOf(item) !== index);

            if (duplicates.length > 0) {
                status += '0';
            } else {
                status += '1';
            }    
        }

        if (status === '111x111') {
            outputEl.classList.remove('fail');
            outputEl.classList.add('success');
            outputEl.textContent = 'Success!';
        } else {
            outputEl.classList.add('fail');
            outputEl.classList.remove('success');
            outputEl.textContent = 'Keep trying...';
        }
    });
}