const getUsers = async () => {
  const rep = await fetch("https://jsonplaceholder.typicode.com/users");
  const users = await rep.json();

  return users;
};

const getUserNames = async () => {
  const Users = await getUsers();
  return Users.map((user) => user.name)
};

const getUsersInCity = async (cityName) => {
  const Users = await getUsers();
  return Users.filter((user) => user.address?.city === cityName)
};

const run = async () => {
  console.log("User count:", (await getUsers()).length);
  console.log("User names:", await getUserNames());
  console.log("Users in city:", await getUsersInCity("Gwenborough"));
};

run();
