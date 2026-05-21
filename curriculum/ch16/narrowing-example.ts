const printValue = (value: string | number): void => {
  if (typeof value === 'string') {
    console.log(value.toUpperCase());
    return;
  }

  console.log(value.toFixed(2));
};

printValue('hello');
printValue(12.5);
