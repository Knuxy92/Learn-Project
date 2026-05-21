const products = [
  { name: "Keyboard", price: 450, inStock: true },
  { name: "Mouse", price: 300, inStock: false },
  { name: "Notebook", price: 300, inStock: true },
];

const productNames = products.map((product) => product.name);
const cheapProducts = products.filter((product) => product.price <= 500);
const foundProduct = products.find((product) => product.name === "Mouse");
const hasExpensiveProduct = products.some((product) => product.price > 1000);
const allInStock = products.every((product) => product.inStock);
const totalPrice = products.reduce((sum, product) => sum + product.price, 0);

console.log("Product names:", productNames);
console.log("Cheap products:", cheapProducts);
console.log("Found product:", foundProduct);
console.log("Has expensive product:", hasExpensiveProduct);
console.log("All in stock:", allInStock);
console.log("Total price:", totalPrice);
