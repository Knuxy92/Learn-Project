const bankAccount = {
  owner: 'Neo',
  balance: 1000,
  getBalance() {
    return this.balance;
  },
};

console.log(bankAccount.getBalance());
