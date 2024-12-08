function attachEvents() {

    const baseUrl = 'http://localhost:3030/jsonstore/messenger';

    const outputEl = document.querySelector('#messages');
    const inputs = document.querySelectorAll('#controls input[name]');
    const buttonSubmitEl = document.querySelector('#submit');
    const buttonRefreshEl = document.querySelector('#refresh');

    buttonSubmitEl.addEventListener('click', (e) => {

        const [ author, content ] = [...inputs].map(field => field.value);

        if ( ! author || ! content ) return;

        const body = { author, content }

        fetch(baseUrl, {
            method: 'POST',
            body: JSON.stringify(body)
        })
            .then(response => response.json())
            .then(result => {
                buttonRefreshEl.click();
            })
            .catch(error => console.error('Error: ', error));

    });

    buttonRefreshEl.addEventListener('click', (e) => {

        outputEl.textContent = '';

        fetch(baseUrl)
            .then(response => response.json())
            .then(messages => {
                
                Object.values(messages).forEach(message => {
                    console.log(message);
                    outputEl.textContent += `${message.author}: ${message.content}\n`
                });

                outputEl.textContent = outputEl.textContent.trimEnd();

            })
            .catch(error => console.error('Error: ', error));

    });

    buttonRefreshEl.click();

}

attachEvents();