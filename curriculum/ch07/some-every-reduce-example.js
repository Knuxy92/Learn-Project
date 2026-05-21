const numbers = [10, 20, 30];

const hasLargeNumber = numbers.some((number) => {
  return number > 25;
});

const allPositive = numbers.every((number) => {
  return number > 0;
});

const total = numbers.reduce((sum, number) => {
  return sum + number;
}, 0);

console.log(hasLargeNumber);
console.log(allPositive);
console.log(total);
