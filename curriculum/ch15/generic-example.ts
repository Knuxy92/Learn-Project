const firstItem = <T>(items: T[]): T | undefined => {
  return items[0];
};

console.log(firstItem(['a', 'b', 'c']));
console.log(firstItem([10, 20, 30]));
