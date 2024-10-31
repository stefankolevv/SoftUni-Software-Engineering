function solve(fruit, weightInGrams, pricePerKg) {
    const weightInKg = weightInGrams /  1000;
    const cost = weightInKg * pricePerKg;
    console.log(`I need $${cost.toFixed(2)} to buy ${weightInKg.toFixed(2)} kilograms ${fruit}.`)
}

// Test Case

solve('orange', 2500, 1.80);
solve('apple', 1563, 2.35);