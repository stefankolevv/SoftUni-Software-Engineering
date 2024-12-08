async function accordion() {
    const main = document.getElementById('main');

    const response = await fetch('http://localhost:3030/jsonstore/advanced/articles/list');
    const articles = await response.json();

    main.innerHTML = '';

    for (const article of articles) {

        const articleResponse = await fetch(`http://localhost:3030/jsonstore/advanced/articles/details/${article._id}`);
        const articleDetails = await articleResponse.json();

        const accordionDiv = document.createElement('div');
        accordionDiv.className = 'accordion';


        const headDiv = document.createElement('div');
        headDiv.className = 'head';
        
        const titleSpan = document.createElement('span');
        titleSpan.textContent = articleDetails.title;

        const button = document.createElement('button');
        button.className = 'button';
        button.textContent = 'More';
        button.id = article._id;

        const extraDiv = document.createElement('div');
        extraDiv.className = 'extra';
        extraDiv.style.display = 'none';

        const contentPara = document.createElement('p');
        contentPara.textContent = articleDetails.content;

        headDiv.appendChild(titleSpan);
        headDiv.appendChild(button);
        extraDiv.appendChild(contentPara);
        accordionDiv.appendChild(headDiv);
        accordionDiv.appendChild(extraDiv);
        main.appendChild(accordionDiv);

        button.addEventListener('click', () => {
            if (extraDiv.style.display === 'none') {
                extraDiv.style.display = 'block';
                button.textContent = 'Less';
            } else {
                extraDiv.style.display = 'none';
                button.textContent = 'More';
            }
        });
    }
}

window.onload = accordion;
