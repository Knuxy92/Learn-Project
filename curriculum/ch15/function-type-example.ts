type MathFn = (firstNumber: number, secondNumber: number) => number;

const multiply: MathFn = (firstNumber, secondNumber) => {
  return firstNumber * secondNumber;
};

console.log(multiply(4, 5));
