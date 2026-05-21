const todos = ["learn JS", "learn Js", "practice code"];

console.log("First todo:", todos[0]);
console.log("Todo count:", todos.length);

todos.push("build project");
console.log("After push:", todos);

todos.pop();
console.log("After pop:", todos);

for (const todo of todos) {
  console.log(todo);
}
