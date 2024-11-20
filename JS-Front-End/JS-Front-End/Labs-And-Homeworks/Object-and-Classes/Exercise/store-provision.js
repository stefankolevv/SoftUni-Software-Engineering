function solve(stock, ordered) {
    
    const storage = [...stock, ...ordered].reduce((storage, product, i, array) => {
        if (i % 2 == 0) storage[product] = (storage[product] || 0) + Number(array[i + 1]);
        return storage;
    }, {});

    for (const product in storage) {
        console.log(`${product} -> ${storage[product]}`);
    }
}

// Test Case

solve(['Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'], ['Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30']);
solve(['Salt', '2', 'Fanta', '4', 'Apple', '14', 'Water', '4', 'Juice', '5'], ['Sugar', '44', 'Oil', '12', 'Apple', '7', 'Tomatoes', '7', 'Bananas', '30']);