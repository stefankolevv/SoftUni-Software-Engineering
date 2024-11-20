function meetings(input) {
    let schedule = {};
    input.forEach(entry => {
        let [day, person] = entry.split(' ');
        if (schedule[day]) {
            console.log(`Conflict on ${day}!`);
        } else {
            schedule[day] = person;
            console.log(`Scheduled for ${day}`);
        }
    });
    for (let day in schedule) {
        console.log(`${day} -> ${schedule[day]}`);
    }
}

// Test Case

meetings(['Monday Peter', 'Wednesday Bill', 'Monday Tim', 'Friday Tim']);
meetings(['Friday Bob', 'Saturday Ted', 'Monday Bill', 'Monday John', 'Wednesday George']);