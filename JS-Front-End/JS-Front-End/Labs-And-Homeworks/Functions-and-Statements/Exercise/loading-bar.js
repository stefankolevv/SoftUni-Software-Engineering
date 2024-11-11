function visalizedLoadingBar(percentage) {
    const barsLength = 10;
    const barsFilled = Math.round(percentage / barsLength);
    const barsEmpty = barsLength - barsFilled;

    const before = (percentage < 100) ? `${percentage}% ` : '100% Complete!\n';
    const progressBar = `[${'%'.repeat(barsFilled)}${'.'.repeat(barsEmpty)}]\n`;
    const after = (percentage < 100) ? 'Still loading...' : '';

    console.log(before + progressBar + after);
}

// Test Case

visalizedLoadingBar(30);
visalizedLoadingBar(50);
visalizedLoadingBar(100);