function catalogue(input) {
    let products = {};

    for (let line of input) {
        let [productName, price] = line.split(' : ');
        price = Number(price);
        let initial = productName[0];

        if (!products[initial]) {
            products[initial] = {};
        }
        products[initial][productName] = price;
    }

    let sortedInitials = Object.keys(products).sort();

    for (let initial of sortedInitials) {
        console.log(initial);
        let sortedProducts = Object.entries(products[initial]).sort((a, b) => a[0].localeCompare(b[0]));
        for (let [productName, price] of sortedProducts) {
            console.log(`  ${productName}: ${price}`);
        }
    }
}

// Test Case

catalogue([
    'Appricot : 20.4',
    'Fridge : 1500',
    'TV : 1499',
    'Deodorant : 10',
    'Boiler : 300',
    'Apple : 1.25',
    'Anti-Bug Spray : 15',
    'T-Shirt : 10'
]);
catalogue([
    'Omlet : 5.4',
    'Shirt : 15',
    'Cake : 59'
]);
