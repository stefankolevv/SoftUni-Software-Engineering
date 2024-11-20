function garage(input) {
    let garages = {};

    input.forEach(entry => {
        let [garageNumber, carInfo] = entry.split(' - ');
        if (!garages[garageNumber]) garages[garageNumber] = [];
        garages[garageNumber].push(
            carInfo
                .split(', ')
                .map(info => info.replace(': ', ' - '))
                .join(', ')
        );
    });

    Object.entries(garages).forEach(([garage, cars]) => {
        console.log(`Garage № ${garage}`);
        cars.forEach(car => console.log(`--- ${car}`));
    });
}

// Test Case

garage(['1 - color: blue, fuel type: diesel', '1 - color: red, manufacture: Audi', '2 - fuel type: petrol', '4 - color: dark blue, fuel type: diesel, manufacture: Fiat']);	
garage(['1 - color: green, fuel type: petrol', '1 - color: dark red, manufacture: WV', '2 - fuel type: diesel', '3 - color: dark blue, fuel type: petrol']);	