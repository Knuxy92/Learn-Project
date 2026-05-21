const calculateTax = (price, rate) => {
  return price * rate;
};

const formatName = (firstName, lastName) => {
  return `${firstName} ${lastName}`;
};

const isEven = (number) => {
  return number % 2 == 0;
};

const greetUser = (userName = "Guest") => {
  return `Hello ${userName}`;
};

console.log(`Tax: ${calculateTax(1000, 0.07)}`);
console.log(`Full name: ${formatName("Knuxy", "Dev")}`);
console.log(`Is 10 even: ${isEven(10)}`);
console.log(`Is 7 even: ${isEven(7)}`);
console.log(greetUser());
console.log(greetUser("Knuxy92"));
