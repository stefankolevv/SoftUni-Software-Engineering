function solve() {
    const infoBox = document.querySelector('#info span');
    const departBtn = document.querySelector('#depart');
    const arriveBtn = document.querySelector('#arrive');

    let currentStop = {
        name: '',
        next: 'depot',
    };

    async function depart() {
        try {

            const response = await fetch(`http://localhost:3030/jsonstore/bus/schedule/${currentStop.next}`);
            if (!response.ok) throw new Error('Stop not found');

            const data = await response.json();

            currentStop = data;
            infoBox.textContent = `Next stop ${currentStop.name}`;

            departBtn.disabled = true;
            arriveBtn.disabled = false;
        } catch (error) {

            infoBox.textContent = 'Error';
            departBtn.disabled = true;
            arriveBtn.disabled = true;
        }
    }

    function arrive() {

        infoBox.textContent = `Arriving at ${currentStop.name}`;

        departBtn.disabled = false;
        arriveBtn.disabled = true;
    }

    return {
        depart,
        arrive
    };
}

let result = solve();
