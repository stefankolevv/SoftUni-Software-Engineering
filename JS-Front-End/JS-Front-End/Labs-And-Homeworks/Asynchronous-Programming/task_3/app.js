function attachEvents() {
    const baseUrl = 'http://localhost:3030/jsonstore/forecaster';
    const locationInput = document.getElementById('location');
    const submitButton = document.getElementById('submit');
    const forecastDiv = document.getElementById('forecast');
    const currentDiv = document.getElementById('current');
    const upcomingDiv = document.getElementById('upcoming');

    const weatherSymbols = {
        'Sunny': '&#x2600;', // ☀
        'Partly sunny': '&#x26C5;', // ⛅
        'Overcast': '&#x2601;', // ☁
        'Rain': '&#x2614;', // ☂
        'Degrees': '&#176;' // °
    };

    submitButton.addEventListener('click', async () => {
        try {

            currentDiv.innerHTML = '<div class="label">Current conditions</div>';
            upcomingDiv.innerHTML = '<div class="label">Three-day forecast</div>';
            forecastDiv.style.display = 'none';

            const location = locationInput.value;
            const locationsResponse = await fetch(`${baseUrl}/locations`);
            if (!locationsResponse.ok) throw new Error('Location not found');
            const locations = await locationsResponse.json();

            const locationData = locations.find(loc => loc.name.toLowerCase() === location.toLowerCase());
            if (!locationData) throw new Error('Invalid location');

            const { code } = locationData;

            const todayResponse = await fetch(`${baseUrl}/today/${code}`);
            if (!todayResponse.ok) throw new Error('Error fetching current weather');
            const todayData = await todayResponse.json();

            const currentForecast = createCurrentConditions(todayData);
            currentDiv.appendChild(currentForecast);

            const upcomingResponse = await fetch(`${baseUrl}/upcoming/${code}`);
            if (!upcomingResponse.ok) throw new Error('Error fetching upcoming weather');
            const upcomingData = await upcomingResponse.json();

            const upcomingForecast = createUpcomingConditions(upcomingData);
            upcomingDiv.appendChild(upcomingForecast);

            forecastDiv.style.display = 'block';
        } catch (error) {
            forecastDiv.style.display = 'block';
            currentDiv.innerHTML = '<div class="label">Error</div>';
        }
    });

    function createCurrentConditions(data) {
        const { forecast, name } = data;

        const conditionDiv = document.createElement('div');
        conditionDiv.className = 'forecasts';

        const symbolSpan = document.createElement('span');
        symbolSpan.className = 'condition symbol';
        symbolSpan.innerHTML = weatherSymbols[forecast.condition];

        const conditionInfo = document.createElement('span');
        conditionInfo.className = 'condition';

        const citySpan = document.createElement('span');
        citySpan.className = 'forecast-data';
        citySpan.textContent = name;

        const tempSpan = document.createElement('span');
        tempSpan.className = 'forecast-data';
        tempSpan.innerHTML = `${forecast.low}${weatherSymbols.Degrees}/${forecast.high}${weatherSymbols.Degrees}`;

        const conditionSpan = document.createElement('span');
        conditionSpan.className = 'forecast-data';
        conditionSpan.textContent = forecast.condition;

        conditionInfo.append(citySpan, tempSpan, conditionSpan);
        conditionDiv.append(symbolSpan, conditionInfo);

        return conditionDiv;
    }

    function createUpcomingConditions(data) {
        const { forecast } = data;

        const upcomingDiv = document.createElement('div');
        upcomingDiv.className = 'forecast-info';

        forecast.forEach(day => {
            const upcomingSpan = document.createElement('span');
            upcomingSpan.className = 'upcoming';

            const symbolSpan = document.createElement('span');
            symbolSpan.className = 'symbol';
            symbolSpan.innerHTML = weatherSymbols[day.condition];

            const tempSpan = document.createElement('span');
            tempSpan.className = 'forecast-data';
            tempSpan.innerHTML = `${day.low}${weatherSymbols.Degrees}/${day.high}${weatherSymbols.Degrees}`;

            const conditionSpan = document.createElement('span');
            conditionSpan.className = 'forecast-data';
            conditionSpan.textContent = day.condition;

            upcomingSpan.append(symbolSpan, tempSpan, conditionSpan);
            upcomingDiv.appendChild(upcomingSpan);
        });

        return upcomingDiv;
    }
}

attachEvents();
