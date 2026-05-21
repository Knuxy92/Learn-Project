const itemName = 'Keyboard';
const itemPrice = 100;
const quantity = 11;

const subtotal = itemPrice * quantity;
const hasDiscount = quantity > 10;
const discountAmount = quantity > 10 ? 0.1*subtotal : 0;
const finalTotal = subtotal-discountAmount;
const discountMessage = discountAmount ? `discount ${discountAmount}` : 'No discount';

console.log(`Item: ${itemName}`);
console.log(`Price: ${itemPrice}`);
console.log(`Quantity: ${quantity}`);
console.log(`Subtotal: ${subtotal}`);
console.log(`Has discount: ${hasDiscount}`);
console.log(`Discount amount: ${discountAmount}`);
console.log(`Final total: ${finalTotal}`);
console.log(discountMessage);
