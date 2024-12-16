function solve(input) {
    const farmersCount = Number(input.shift()); // Extracting the num of farmers from the input by converting it to a num...
    const farmersInput = input.splice(0, farmersCount);

    const farmers = farmersInput.reduce((acc, farmerDetails) => {
        const [name, workArea, tasks] = farmerDetails.split(' ');
        acc[name] = {
            workArea,
            tasks: tasks.split(',').sort()
        };
        return acc;
    }, {});

    input.forEach(commandLine => {
        if (commandLine === 'End') return;

        const [command, farmerName, param1, param2] = commandLine.split(' / ');

        switch (command) {
            case 'Execute': {
                const [workArea, task] = [param1, param2];

                if (
                    farmers[farmerName].workArea === workArea &&
                    farmers[farmerName].tasks.includes(task)
                ) {
                    console.log(`${farmerName} has executed the task: ${task}!`);
                } else {
                    console.log(`${farmerName} cannot execute the task: ${task}.`);
                }
                break;
            }

            case 'Change Area': {
                const newWorkArea = param1;
                farmers[farmerName].workArea = newWorkArea;
                console.log(`${farmerName} has changed their work area to: ${newWorkArea}`);
                break;
            }

            case 'Learn Task': {
                const newTask = param1;

                if (farmers[farmerName].tasks.includes(newTask)) {
                    console.log(`${farmerName} already knows how to perform ${newTask}.`);
                } else {
                    farmers[farmerName].tasks.push(newTask);
                    farmers[farmerName].tasks.sort(); // Sorting the farmer's tasks in alphabetical order for easier reading & comparison...
                    console.log(`${farmerName} has learned a new task: ${newTask}.`);
                }
                break;
            }
        }
    });

    // Iterating through all farmers to print their final data:
    Object.entries(farmers).forEach(([name, { workArea, tasks }]) => {
        console.log(`Farmer: ${name}, Area: ${workArea}, Tasks: ${tasks.join(', ')}`);
    });
}

// Test Case

solve([
    "2",
    "John garden watering,weeding",
    "Mary barn feeding,cleaning",
    "Execute / John / garden / watering",
    "Execute / Mary / garden / feeding",
    "Learn Task / John / planting",
    "Execute / John / garden / planting",
    "Change Area / Mary / garden",
    "Execute / Mary / garden / cleaning",
    "End"
]);
console.log('---');
solve([
    "3",
    "Alex apiary harvesting,honeycomb",
    "Emma barn milking,cleaning",
    "Chris garden planting,weeding",
    "Execute / Alex / apiary / harvesting",
    "Learn Task / Alex / beeswax",
    "Execute / Alex / apiary / beeswax",
    "Change Area / Emma / apiary",
    "Execute / Emma / apiary / milking",
    "Execute / Chris / garden / watering",
    "Learn Task / Chris / pruning",
    "Execute / Chris / garden / pruning",
    "End"
  ]
  );