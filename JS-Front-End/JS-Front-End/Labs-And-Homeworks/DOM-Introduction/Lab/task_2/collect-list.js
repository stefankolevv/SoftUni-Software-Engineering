function extractText() {
    const listElements = document.querySelectorAll('ul li');
    const textareaElement = document.querySelector('#result');

    textareaElement.value = [...listElements].map(el => el.textContent.trim()).join('\n');
}