function flightSchedule(input) {
    let [flights, statusChanges, statusToCheck] = input;
    let flightMap = {};

    flights.forEach(flight => {
        let indexOfSpace = flight.indexOf(' ');
        let flightNumber = flight.slice(0, indexOfSpace);
        let destination = flight.slice(indexOfSpace + 1);
        flightMap[flightNumber] = { Destination: destination, Status: 'Ready to fly' };
    });

    statusChanges.forEach(change => {
        let [flightNumber, newStatus] = change.split(' ');
        if (flightMap[flightNumber]) {
            flightMap[flightNumber].Status = newStatus;
        }
    });

    Object.values(flightMap)
        .filter(flight => flight.Status === statusToCheck[0])
        .forEach(flight => console.log(flight));
}

// Test Case

flightSchedule([['WN269 Delaware',
    'FL2269 Oregon',
     'WN498 Las Vegas',
     'WN3145 Ohio',
     'WN612 Alabama',
     'WN4010 New York',
     'WN1173 California',
     'DL2120 Texas',
     'KL5744 Illinois',
     'WN678 Pennsylvania'],
     ['DL2120 Cancelled',
     'WN612 Cancelled',
     'WN1173 Cancelled',
     'SK430 Cancelled'],
     ['Cancelled']
]);
flightSchedule([['WN269 Delaware',
    'FL2269 Oregon',
     'WN498 Las Vegas',
     'WN3145 Ohio',
     'WN612 Alabama',
     'WN4010 New York',
     'WN1173 California',
     'DL2120 Texas',
     'KL5744 Illinois',
     'WN678 Pennsylvania'],
     ['DL2120 Cancelled',
     'WN612 Cancelled',
     'WN1173 Cancelled',
     'SK330 Cancelled'],
     ['Ready to fly']
]);