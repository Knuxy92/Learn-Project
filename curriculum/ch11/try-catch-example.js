try {
  JSON.parse('{ bad json }');
} catch (error) {
  console.log(error.name);
  console.log(error.message);
}
