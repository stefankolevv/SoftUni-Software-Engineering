function createElement(tag, properties, container) {
    const element = document.createElement(tag);

    Object.keys(properties).forEach(property => {
        if (typeof properties[property] === 'object') {
            Object.assign(element.dataset, properties[property]);
        } else {
            element[property] = properties[property];
        }
    });

    if (container) container.appendChild(element);

    return element;
}

async function getInfo() {
    const stopIdInput = document.getElementById('stopId');
    const stopNameDiv = document.getElementById('stopName');
    const busesList = document.getElementById('buses');

    stopNameDiv.textContent = '';
    busesList.innerHTML = '';

    const stopId = stopIdInput.value;

    try {
        const response = await fetch(`http://localhost:3030/jsonstore/bus/businfo/${stopId}`);
        if (!response.ok) throw new Error('Invalid Stop ID');

        const data = await response.json();

        stopNameDiv.textContent = data.name;

        Object.entries(data.buses).forEach(([busId, time]) => {
            createElement('li', { textContent: `Bus ${busId} arrives in ${time} minutes` }, busesList);
        });
    } catch (error) {
        stopNameDiv.textContent = 'Error';
    }
}
