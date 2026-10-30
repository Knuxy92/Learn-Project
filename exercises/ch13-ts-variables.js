var userName = 'Student';
var userAge = 17;
var isStudent = true;
var formatProfile = function (name, age, studentStatus) {
    return "".concat(name, " - ").concat(age, " - ").concat(studentStatus);
};
console.log(userName);
console.log(userAge);
console.log(isStudent);
console.log(formatProfile(userName, userAge, isStudent));
