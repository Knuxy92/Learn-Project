const formatUserName = (userName) => userName.trim().toUpperCase();

const isValidEmail = (email) => /@.*\./.test(email);

const getPasswordStrength = (password) =>
  password.length < 8 ? "weak" : "strong";

const formatWelcomeMessage = (firstName, lastName) =>
  `Welcome ${firstName} ${lastName}`;

const formatToday = () => new Date().toLocaleDateString();

console.log(`Formatted user name: ${formatUserName("  knuxy92  ")}`);
console.log(`Valid email (yes): ${isValidEmail("test@example.com")}`);
console.log(`Valid email (no): ${isValidEmail("testexample")}`);
console.log(`Password strength: ${getPasswordStrength("secret123")}`);
console.log(`Welcome: ${formatWelcomeMessage("Student", "Dev")}`);
console.log(`Today: ${formatToday()}`);
