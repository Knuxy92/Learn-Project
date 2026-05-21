const userName: string = 'Knuxy92';
const userAge: number = 17;
const isStudent: boolean = true;

const formatProfile = (
  name: string,
  age: number,
  studentStatus: boolean,
): string => {
  return `${name} - ${age} - ${studentStatus}`;
};

console.log(userName);
console.log(userAge);
console.log(isStudent);
console.log(formatProfile(userName, userAge, isStudent));
