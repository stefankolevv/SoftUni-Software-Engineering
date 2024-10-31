function solve(num, op1, op2, op3, op4, op5) {

    for (let i = 1; i <= 5; i++) {
        switch(eval('op' + i)) {
            case 'chop':
                num /= 2;
                break;
            case 'dice':
                num = Math.sqrt(num);
                break;
            case 'spice':
                num++
                break;
            case 'bake':
                num *= 3;
                break;
            case 'fillet':
                num *= 0.8;
                break;
        }

        if ( ! Number.isInteger(num) ) num = num.toFixed(2);
            console.log(num);
    }
}

// Test Case

solve('32', 'chop', 'chop', 'chop', 'chop', 'chop');
solve('9', 'dice', 'spice', 'chop', 'bake', 'fillet');