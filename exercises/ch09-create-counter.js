const createCounter = () => {
  let count = 0;

  return {
    increment() {
      count += 1
      return count;
    },
    decrement() {
      count -= 1
      return count;
    },
    getCount() {
      return count;
    },
  };
};

const sumAll = (...numbers) => {
  return numbers.reduce((sum, number) => sum + number, 0);
};

const counter = createCounter();
const values = [10, 20, 30];

console.log(`Count: ${counter.getCount()}`);
console.log(`After increment: ${counter.increment()}`);
console.log(`After increment again: ${counter.increment()}`);
console.log(`After decrement: ${counter.decrement()}`);
console.log(`Current count: ${counter.getCount()}`);
console.log(`Sum all: ${sumAll(...values)}`);
