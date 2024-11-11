function calculateOrderPrice(product, quantity) {
    
    const drinks = [];

    drinks['coffee'] = (q) => q * 1.50;
    drinks['water'] = (q) => q * 1.00;
    drinks['coke'] = (q) => q * 1.40;
    drinks['snacks'] = (q) => q * 2.00;

    console.log(drinks[product](quantity).toFixed(2));
}

// Test Case

calculateOrderPrice("water", 5);
calculateOrderPrice("coffee", 2);