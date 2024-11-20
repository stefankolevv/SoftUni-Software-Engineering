function piccolo(arr) {
    const parking = new Set();

    arr.forEach(log => {
        const [direction, carNumber] = log.split(', ');
        if (direction === 'IN') {
            parking.add(carNumber);
        } else {
            parking.delete(carNumber);
        }
    });

    console.log(parking.size
        ? [...parking].sort().join('\n')
        : 'Parking Lot is Empty');
}
