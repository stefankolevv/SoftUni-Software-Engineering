function extract(elementId) {
    const text = document.querySelector('#' + elementId).textContent.trim();
    const pattern = /\(([^()]+)\)/g;
    const output = [...text.matchAll(pattern)].map(el => el[1]).join('; ');

    console.log(output);
    
    return output;
}