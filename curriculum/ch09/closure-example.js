const createCounter = () => {
  let count = 0;

  return () => {
    count += 1;
    return count;
  };
};

const counter = createCounter();

console.log(counter());
console.log(counter());
