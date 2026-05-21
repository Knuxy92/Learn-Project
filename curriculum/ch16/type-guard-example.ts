const isString = (value: unknown): value is string => {
  return typeof value === 'string';
};

console.log(isString('hello'));
console.log(isString(123));
