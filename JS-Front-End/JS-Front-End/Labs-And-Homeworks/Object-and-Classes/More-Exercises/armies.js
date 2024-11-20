function armies(input) {
    let leaders = {};

    input.forEach(line => {
        if (line.includes('arrives')) {
            let leader = line.split(' arrives')[0];
            if (!leaders[leader]) leaders[leader] = { total: 0, armies: {} };
        } else if (line.includes(':')) {
            let [leader, rest] = line.split(': ');
            if (leaders[leader]) {
                let [armyName, armyCount] = rest.split(', ');
                leaders[leader].armies[armyName] = Number(armyCount);
                leaders[leader].total += Number(armyCount);
            }
        } else if (line.includes('+')) {
            let [armyName, armyCount] = line.split(' + ');
            Object.values(leaders).forEach(leader => {
                if (leader.armies[armyName] !== undefined) {
                    leader.armies[armyName] += Number(armyCount);
                    leader.total += Number(armyCount);
                }
            });
        } else if (line.includes('defeated')) {
            let leader = line.split(' defeated')[0];
            delete leaders[leader];
        }
    });

    Object.entries(leaders)
        .sort((a, b) => b[1].total - a[1].total)
        .forEach(([leader, data]) => {
            console.log(`${leader}: ${data.total}`);
            Object.entries(data.armies)
                .sort((a, b) => b[1] - a[1])
                .forEach(([army, count]) => console.log(`>>> ${army} - ${count}`));
        });
}

// Test Case

armies(['Rick Burr arrives', 'Fergus: Wexamp, 30245', 'Rick Burr: Juard, 50000', 'Findlay arrives', 'Findlay: Britox, 34540', 'Wexamp + 6000', 'Juard + 1350', 'Britox + 4500', 'Porter arrives', 'Porter: Legion, 55000', 'Legion + 302', 'Rick Burr defeated', 'Porter: Retix, 3205']);	
// Porter: 58507
// >>> Legion - 55302
// >>> Retix - 3205
// Findlay: 39040
// >>> Britox - 39040
armies(['Rick Burr arrives', 'Findlay arrives', 'Rick Burr: Juard, 1500', 'Wexamp arrives', 'Findlay: Wexamp, 34540', 'Wexamp + 340', 'Wexamp: Britox, 1155', 'Wexamp: Juard, 43423']);	
// Wexamp: 44578
// >>> Juard - 43423
// >>> Britox - 1155
// Findlay: 34880
// >>> Wexamp - 34880
// Rick Burr: 1500
// >>> Juard - 1500
