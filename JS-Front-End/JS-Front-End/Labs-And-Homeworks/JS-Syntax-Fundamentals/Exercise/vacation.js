function solve(numberOfPeople, groupType, dayOfTheWeek) {

    const sFriday = 8.45;
    const sSaturday = 9.80;
    const sSunday = 10.46;

    const bFriday = 10.90;
    const bSaturday = 15.60;
    const bSunday = 16;

    const rFriday = 15;
    const rSaturday = 20;
    const rSunday = 22.50;

    let price;

    switch (groupType) {
        case 'Students':

            switch(dayOfTheWeek) {
                case 'Friday':
                    price = numberOfPeople * sFriday
                    break;
                case 'Saturday':
                    price = numberOfPeople * sSaturday
                    break;
                case 'Sunday':
                    price = numberOfPeople * sSunday
                    break;
            }

            if (numberOfPeople >= 30) price *= 0.85;

            break;
        case 'Business':
            
            if (numberOfPeople >= 100) numberOfPeople -= 10;

            switch(dayOfTheWeek) {
                case 'Friday':
                    price = numberOfPeople * bFriday
                    break;
                case 'Saturday':
                    price = numberOfPeople * bSaturday
                    break;
                case 'Sunday':
                    price = numberOfPeople * bSunday
                    break;
        }

            break;
        case 'Regular':

            switch(dayOfTheWeek) {
                case 'Friday':
                    price = numberOfPeople * rFriday
                    break;
                case 'Saturday':
                    price = numberOfPeople * rSaturday
                    break;
                case 'Sunday':
                    price = numberOfPeople * rSunday
                    break;
                
        }

        if (numberOfPeople >= 10 && numberOfPeople <= 20) price *= 0.95;

                break;
    }

    console.log(`Total price: ${price.toFixed(2)}`)
}

// Test Case

solve(30, "Students", "Sunday");
solve(40, "Regular", "Saturday");