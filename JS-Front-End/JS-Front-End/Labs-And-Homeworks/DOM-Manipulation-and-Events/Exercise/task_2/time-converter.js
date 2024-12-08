document.addEventListener('DOMContentLoaded', solve);

function solve() {
    
    const values = {days: 86400, hours: 3600, minutes: 60, seconds: 1}

    const inputElDays = document.querySelector('#days-input');
    const inputElHours = document.querySelector('#hours-input');
    const inputElMinutes = document.querySelector('#minutes-input');
    const inputElSeconds = document.querySelector('#seconds-input');

    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', handleSubmitEvent)
    });

    function handleSubmitEvent(e) {
        e.preventDefault();

        const currentInputEl = e.target.querySelector('input[type="number"]');
        const currentValue = Number(currentInputEl.value);

        if (currentValue < 1) return;

        const key = currentInputEl.getAttribute('id').split('-input')[0];
        const miltiplier = values[key];

        updateValues(currentValue * miltiplier);
    }

    function updateValues(secondAmount) {
        inputElDays.value = Number(secondAmount / values.days).toFixed(2);
        inputElHours.value = Number(secondAmount / values.hours).toFixed(2);
        inputElMinutes.value = Number(secondAmount / values.minutes).toFixed(2);
        inputElSeconds.value = Number(secondAmount / values.seconds).toFixed(2);
    }
}