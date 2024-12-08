document.addEventListener('DOMContentLoaded', solve);

function solve() {
    
    document.querySelector('main').addEventListener('click', (e) => {
        
        if (e.target.nodeName !== 'BUTTON') return;

        const profileEl = e.target.closest('.profile');
        const state = profileEl.querySelector('input[name*="locked"]:checked').getAttribute('id');
        
        if (state.includes('Lock')) return;

        const hiddenFieldsEl = profileEl.querySelector('.hidden-fields');

        if (hiddenFieldsEl.classList.contains('active')) {
            hiddenFieldsEl.classList.remove('active');
            e.target.textContent = 'Show less';
        } else {
            hiddenFieldsEl.classList.add('active');
            e.target.textContent = 'Show more';
        }
    });
}