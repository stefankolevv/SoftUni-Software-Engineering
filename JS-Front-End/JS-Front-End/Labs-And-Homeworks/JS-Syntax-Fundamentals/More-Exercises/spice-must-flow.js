function spiceMustFlow(yield) {
    let days = 0, totalSpice = 0;

    while (yield >= 100) {
        totalSpice += yield - 26;
        yield -= 10;
        days++;
    }
    totalSpice = Math.max(0, totalSpice - 26);
    console.log(days);
    console.log(totalSpice);
}

// Test Case

spiceMustFlow(111);
spiceMustFlow(450);