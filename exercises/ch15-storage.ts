type MathFn = (firstNumber: number, secondNumber: number) => number;

const subtract: MathFn = (firstNumber: number, secondNumber: number):number => {
  return firstNumber - secondNumber;
};

const firstItem = <T>(items: T[]): T | undefined => {
  return items[0];
};

type User = {
  id: number;
  name: string;
  email: string;
  age: number;
};

type UserPreview = Pick<User, 'id' | 'name'>;
type UserWithoutEmail = Omit<User, 'email'>;

const userPreview: UserPreview = {
  id: 1,
  name: 'Knuxy92',
};

const userWithoutEmail: UserWithoutEmail = {
  id: 2,
  name: 'Xmaol',
  age: 17,
};

console.log(subtract(10, 3));
console.log(firstItem(['a', 'b', 'c']));
console.log(firstItem([10, 20, 30]));
console.log(userPreview);
console.log(userWithoutEmail);
