const itemPrice = 100;
const quantity = 3;
const subtotal = itemPrice * quantity;
const isLargeOrder = quantity > 10;

console.log(subtotal);
console.log(isLargeOrder);
console.log(quantity >= 1 && itemPrice > 0);
