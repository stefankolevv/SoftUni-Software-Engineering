function attachGradientEvents() {
    const resultEl = document.querySelector('#result');
    const gradientEl = document.querySelector('#gradient');

    gradientEl.addEventListener('mousemove', (e) => {
        const currentPos = e.offsetX;
        const elementWidth = e.currentTarget.clientWidth;

        console.log(currentPos, elementWidth);

        const percent = Math.floor((currentPos / elementWidth) * 100);
        
        resultEl.textContent = percent + '%';
    });
}
