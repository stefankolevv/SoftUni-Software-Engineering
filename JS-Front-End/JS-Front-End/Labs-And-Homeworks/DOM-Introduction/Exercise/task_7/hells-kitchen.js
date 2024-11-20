function solve() {
    
    const input = document.querySelector('#inputs textarea').value;

    const outputBestRestEl = document.querySelector('#outputs #bestRestaurant p');
    const outputWorkersEl = document.querySelector('#outputs #workers p');

    if ( ! input ) return;

    console.log(input);

    const restorants = JSON.parse(input)
        .reduce((acc, entry) => {
           
            const [ name, workersData ] = entry.split(' - ');
            
            const workers = workersData.split(', ')
                .map(workerData => {

                    const [ name, salary ] = workerData.split(' ');

                    return { name, salary: Number(salary) }
                });

            acc[name] ??= { workers: [] }
            acc[name].workers.push(...workers);

            return acc;
            
        }, {})

        console.log(restorants);

    function getAvgSalary(restoarantData) {
        const allSalaries = restoarantData.workers.reduce((allSalaries, w) => allSalaries + w.salary, 0);
        return allSalaries / restoarantData.workers.length; 
    }

    const [ bestRestorantKey ] = Object.keys(restorants)
        .sort((a, b) => getAvgSalary(restorants[b]) - getAvgSalary(restorants[a]));

    const bestWorkers = restorants[bestRestorantKey].workers
        .toSorted((a, b) => b.salary - a.salary);

    outputBestRestEl.textContent = `Name: ${bestRestorantKey} `;
    outputBestRestEl.textContent += `Average Salary: ${getAvgSalary(restorants[bestRestorantKey]).toFixed(2)} `
    outputBestRestEl.textContent += `Best Salary: ${bestWorkers[0].salary.toFixed(2)}`;

    outputWorkersEl.textContent = bestWorkers.map(w => `Name: ${w.name} With Salary: ${w.salary}`).join(' ');

}