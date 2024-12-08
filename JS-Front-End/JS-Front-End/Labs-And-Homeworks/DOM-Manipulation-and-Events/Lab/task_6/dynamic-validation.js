document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const emailEl = document.querySelector('#email');
    const pattern = /[a-z]+@[a-z]+\.[a-z]+/

    emailEl.addEventListener('change', (event) => {

        if ( ! pattern.test(event.currentTarget.value)) {
            return event.currentTarget.classList.add('error');
        }

        event.currentTarget.classList.remove('error');
    });
}
