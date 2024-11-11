function solve(array) {

    const [username, ...passwords] = array;

    passwords.forEach(function(password, index) {
        if (password === Array.from(username).reverse().join('')) {
            console.log(`User ${username} logged in.`);
        } else if (index >= 3) {
            console.log(`User ${username} blocked!`);
        } else {
            console.log('Incorrect password. Try again.');
        }
    });
}


// Test Case

solve(['Acer', 'login', 'go', 'let me in', 'recA']);
solve(['momo', 'omom']);
solve(['sunny', 'rainy', 'cloudy', 'sunny', 'not sunny']);