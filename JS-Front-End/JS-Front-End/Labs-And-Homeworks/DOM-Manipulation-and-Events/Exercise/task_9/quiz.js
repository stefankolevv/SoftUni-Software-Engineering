document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const sections = Array.from(document.querySelectorAll('.question'));
    const resultsDiv = document.getElementById('results');
    const rightAnswers = [
        'onclick',
        'JSON.stringify()',
        'A programming API for HTML and XML documents'
    ];

    let currentQuestion = 0;
    let correctAnswers = 0;

    sections.forEach((section, index) => {
        const answers = section.querySelectorAll('.quiz-answer');
        answers.forEach(answer => {
            answer.addEventListener('click', () => {

                if (answer.textContent === rightAnswers[index]) {
                    correctAnswers++;
                }

                section.classList.add('hidden');
                if (index + 1 < sections.length) {
                    sections[index + 1].classList.remove('hidden');
                } else {
                    displayResults(correctAnswers);
                }
            });
        });
    });

    function displayResults(correctAnswers) {
        let resultText = '';
        if (correctAnswers === rightAnswers.length) {
            resultText = 'You are recognized as top JavaScript fan!';
        } else if (correctAnswers === 1) {
            resultText = 'You have 1 right answer.';
        } else {
            resultText = `You have ${correctAnswers} right answers.`;
        }
        resultsDiv.textContent = resultText;
        resultsDiv.style.fontSize = '24px';
        resultsDiv.style.marginTop = '20px';
    }
}