document.addEventListener('DOMContentLoaded', solve);

function solve() {
    document.getElementById('convert').addEventListener('click', () => {
        const inputDistance = Number(document.getElementById('inputDistance').value);
        const inputUnits = document.getElementById('inputUnits').value;
        const outputUnits = document.getElementById('outputUnits').value;

        const conversionRates = {
            km: 1000,
            m: 1,
            cm: 0.01,
            mm: 0.001,
            mi: 1609.34,
            yrd: 0.9144,
            ft: 0.3048,
            in: 0.0254
        };

        const valueInMeters = inputDistance * conversionRates[inputUnits];
        const outputDistance = valueInMeters / conversionRates[outputUnits];

        document.getElementById('outputDistance').value = outputDistance.toFixed(2);
    });
}