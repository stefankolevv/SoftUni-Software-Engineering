function movies(arr) {
    let movies = [];

    arr.forEach(command => {
        if (command.startsWith('addMovie')) {
            const name = command.replace('addMovie ', '');
            movies.push({ name });
        } else if (command.includes('directedBy')) {
            const [name, director] = command.split(' directedBy ');
            const movie = movies.find(m => m.name === name);
            if (movie) movie.director = director;
        } else if (command.includes('onDate')) {
            const [name, date] = command.split(' onDate ');
            const movie = movies.find(m => m.name === name);
            if (movie) movie.date = date;
        }
    });

    movies.filter(m => m.name && m.director && m.date).forEach(m => console.log(JSON.stringify(m)));
}

// Test Case

movies([
    'addMovie Fast and Furious',
    'addMovie Godfather',
    'Inception directedBy Christopher Nolan',
    'Godfather directedBy Francis Ford Coppola',
    'Godfather onDate 29.07.2018',
    'Fast and Furious onDate 30.07.2018',
    'Batman onDate 01.08.2018',
    'Fast and Furious directedBy Rob Cohen'
]);	
movies([
    'addMovie The Avengers',
    'addMovie Superman',
    'The Avengers directedBy Anthony Russo',
    'The Avengers onDate 30.07.2010',
    'Captain America onDate 30.07.2010',
    'Captain America directedBy Joe Russo'
]);    