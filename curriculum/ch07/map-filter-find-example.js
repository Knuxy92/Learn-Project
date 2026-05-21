const numbers = [1, 2, 3, 4];

const doubledNumbers = numbers.map((number) => {
  return number * 2;
});

const evenNumbers = numbers.filter((number) => {
  return number % 2 === 0;
});

const foundNumber = numbers.find((number) => {
  return number > 2;
});

console.log(doubledNumbers);
console.log(evenNumbers);
console.log(foundNumber);
