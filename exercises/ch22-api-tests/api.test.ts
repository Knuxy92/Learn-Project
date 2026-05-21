import { test, after } from "node:test";
import assert from "node:assert/strict";
import { app } from "../ch24-task-api-sqlite/app";


const server = app.listen(3001, () => {
  console.log("Server running on port 3001");
});

after(async () => {
  await new Promise<void>((resolve, reject) => {
      server.close((error) => {
        if (error) reject(error);
        else resolve();
      });
    });
})


test("GET /tasks", async () => {
  const response = await fetch("http://localhost:3001/tasks");
  const data = await response.json();

  assert.equal(response.status, 200);
  assert.ok(Array.isArray(data));
});

test("POST /tasks", async () => {
  const response = await fetch("http://localhost:3001/tasks", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      title: "Testing Api",
      done: false,
    }),
  });

  assert.equal(response.status, 200);
});

test("PUT /tasks/999", async () => {
  const response = await fetch("http://localhost:3001/tasks/999", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
  });

  assert.equal(response.status, 404);
});

test("DELETE /tasks/999", async () => {
  const response = await fetch("http://localhost:3001/tasks/999", {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
  });
  
  assert.equal(response.status, 404);
});
