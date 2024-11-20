function comments(input) {
    let users = new Set();
    let articles = {};
    
    input.forEach(line => {
        if (line.startsWith('user ')) {
            users.add(line.split(' ')[1]);
        } else if (line.startsWith('article ')) {
            let articleName = line.split(' ')[1];
            if (!articles[articleName]) {
                articles[articleName] = [];
            }
        } else {
            let [userAndArticle, comment] = line.split(': ');
            let [username, articleName] = userAndArticle.split(' posts on ');
            if (users.has(username) && articles[articleName]) {
                let [title, content] = comment.split(', ');
                articles[articleName].push({ username, title, content });
            }
        }
    });

    let sortedArticles = Object.entries(articles).sort((a, b) => b[1].length - a[1].length);
    
    for (let [article, comments] of sortedArticles) {
        console.log(`Comments on ${article}`);
        comments
            .sort((a, b) => a.username.localeCompare(b.username))
            .forEach(c => {
                console.log(`--- From user ${c.username}: ${c.title} - ${c.content}`);
            });
    }
}

// Test Case
comments(['user aUser123', 'someUser posts on someArticle: NoTitle, stupidComment', 'article Books', 'article Movies', 'article Shopping', 'user someUser', 'user uSeR4', 'user lastUser', 'uSeR4 posts on Books: I like books, I do really like them', 'uSeR4 posts on Movies: I also like movies, I really do', 'someUser posts on Shopping: title, I go shopping every day', 'someUser posts on Movies: Like, I also like movies very much']);
comments(['user Mark', 'Mark posts on someArticle: NoTitle, stupidComment', 'article Bobby', 'article Steven', 'user Liam', 'user Henry', 'Mark posts on Bobby: Is, I do really like them', 'Mark posts on Steven: title, Run', 'someUser posts on Movies: Like']);