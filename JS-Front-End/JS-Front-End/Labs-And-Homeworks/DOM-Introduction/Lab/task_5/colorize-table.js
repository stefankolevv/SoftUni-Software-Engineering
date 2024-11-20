function colorize() {
    const rows = document.querySelectorAll('table tr:nth-child(odd)');
    [...rows].forEach((el, i) => el.style.background = 'teal');
}