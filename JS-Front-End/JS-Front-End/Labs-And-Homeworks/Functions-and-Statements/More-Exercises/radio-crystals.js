function radioCrystals(thicknesses) {
    const targetThickness = thicknesses.shift();

    for (let thickness of thicknesses) {
        console.log(`Processing chunk ${thickness} microns`);

        thickness = processOperation(thickness, 'Cut', n => n / 4);
        thickness = processOperation(thickness, 'Lap', n => n * 0.8);
        thickness = processOperation(thickness, 'Grind', n => n - 20);
        thickness = processOperation(thickness, 'Etch', n => n - 2);

        if (thickness + 1 === targetThickness) {
            thickness += 1;
            console.log('X-ray x1');
        }

        console.log(`Finished crystal ${targetThickness} microns`);

        function processOperation(thickness, operation, performOperation) {
            let count = 0;
            while (performOperation(thickness) >= targetThickness || Math.floor(thickness) - targetThickness === 1) {
                thickness = performOperation(thickness);
                count++;
            }
            if (count > 0) {
                console.log(`${operation} x${count}`);
                console.log('Transporting and washing');
                thickness = Math.floor(thickness);
            }
            return thickness;
        }
    }
}

// Test Case

radioCrystals([1375, 50000]);
radioCrystals([1000, 4000, 8100]);