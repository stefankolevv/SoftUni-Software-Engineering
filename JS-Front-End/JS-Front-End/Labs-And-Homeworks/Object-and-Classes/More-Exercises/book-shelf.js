function bookShelf(input) {
    let shelves = {};

    input.forEach(line => {
        if (line.includes('->')) {
            let [id, genre] = line.split(' -> ');
            if (!shelves[id]) {
                shelves[id] = { genre, books: [] };
            }
        } else {
            let [bookInfo, genre] = line.split(', ');
            let [title, author] = bookInfo.split(': ');
            for (let id in shelves) {
                if (shelves[id].genre === genre) {
                    shelves[id].books.push({ title, author });
                }
            }
        }
    });

    let sortedShelves = Object.entries(shelves).sort((a, b) => b[1].books.length - a[1].books.length);
    
    for (let [id, shelf] of sortedShelves) {
        console.log(`${id} ${shelf.genre}: ${shelf.books.length}`);
        shelf.books
            .sort((a, b) => a.title.localeCompare(b.title))
            .forEach(book => console.log(`--> ${book.title}: ${book.author}`));
    }
}

// Test Case

bookShelf(['1 -> history', '1 -> action', 'Death in Time: Criss Bell, mystery', '2 -> mystery', '3 -> sci-fi', 'Child of Silver: Bruce Rich, mystery', 'Hurting Secrets: Dustin Bolt, action', 'Future of Dawn: Aiden Rose, sci-fi', 'Lions and Rats: Gabe Roads, history', '2 -> romance', 'Effect of the Void: Shay B, romance', 'Losing Dreams: Gail Starr, sci-fi', 'Name of Earth: Jo Bell, sci-fi', 'Pilots of Stone: Brook Jay, history']);
bookShelf(['1 -> mystery', '2 -> sci-fi',
'Child of Silver: Bruce Rich, mystery',
'Lions and Rats: Gabe Roads, history',
'Effect of the Void: Shay B, romance',
'Losing Dreams: Gail Starr, sci-fi',
'Name of Earth: Jo Bell, sci-fi']);	