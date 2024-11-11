function solve(goldMinedPerDay) {

    const priceGold = 67.51;
    const priceBitcoin = 11949.16;

    let bitcoinCount = 0;
    let bitcoinDayIndex = 0;

    const currencyCount = goldMinedPerDay.reduce(function(earnings, dailyGold, i) {
        const currentDay = i + 1;
        let bitcoinDayCount = 0;

        if (currentDay > 0 && currentDay % 3 == 0) dailyGold -= dailyGold * 0.3;

        earnings += dailyGold * priceGold;

        bitcoinDayCount = Math.floor(earnings / priceBitcoin);

        if (bitcoinDayCount) {
            if (! bitcoinDayIndex) bitcoinDayIndex = currentDay;
            earnings -= (bitcoinDayCount * priceBitcoin);
            bitcoinCount += bitcoinDayCount;
        }

        return earnings;
    }, 0);

    console.log(`Bought bitcoins: ${bitcoinCount}`);
    if (bitcoinDayIndex) console.log(`Day of the first purchased bitcoin: ${bitcoinDayIndex}`);
    console.log(`Left money: ${currencyCount.toFixed(2)} lv.`);
}

// Test Case

solve([100, 200, 300]);
solve([50, 100]);
solve([3124.15, 504.212, 2511.124]);