function editElement(element, match, replacer) {
    element.textContent = element.textContent.replaceAll(match, replacer);
}