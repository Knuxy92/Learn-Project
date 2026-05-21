const getMessage = async () => {
  return 'Hello';
};

const run = async () => {
  const message = await getMessage();
  console.log(message);
};

run();
