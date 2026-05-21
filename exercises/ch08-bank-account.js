const bankAccount = {
  owner: "Knuxy92",
  balance: 1000,
  currency: "THB",
};


bankAccount.isActive = true;
bankAccount.deposit = (amount) => bankAccount.balance += amount;
bankAccount.withdraw = (amount) => bankAccount.balance -= amount;
bankAccount.getBalance = () => bankAccount.balance;
const { owner, currency } = bankAccount;

console.log("Owner:", bankAccount.owner);
console.log("Balance before:", bankAccount.balance);
bankAccount.balance = 5000;
console.log("Balance after update:", bankAccount.balance);
bankAccount.deposit(500)
console.log("Balance after deposit:", bankAccount.balance);
bankAccount.withdraw(1000)
console.log("Balance after withdraw:", bankAccount.balance);
console.log("Current balance:", bankAccount.balance);

const accountSummary = {
  ...bankAccount,
  bankname: "My Bank"
};

console.log("Destructured owner:", owner);
console.log("Destructured currency:", currency);
console.log("Account summary:", accountSummary);
 