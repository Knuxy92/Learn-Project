# Chapter Status

## Active Chapter

- Chapter: `Ch27 - Timestamps and Richer Schema`
- Status: `active`
- Main goal: expand the SQLite task schema with timestamp fields and map them cleanly

## Ch1 Checklist

- [x] Node.js is available
- [x] Create first `.js` example
- [x] Create first guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch1 Summary

- JavaScript code can run with Node.js.
- `console.log()` prints output to the terminal.
- Files in `curriculum/` are examples and lessons.
- Files in `exercises/` are for student work.

## Ch2 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch2 Summary

- `const` is for values we do not plan to reassign.
- `let` is for values that need reassignment.
- Basic data types include string, number, boolean, null, and undefined.
- `typeof null` returns `object`, which is a weird old JavaScript behavior.
- Type coercion can make `'5' + 3` become `'53'`, while `'5' - 3` becomes `2`.

## Ch3 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch3 Summary

- Arithmetic operators calculate values like subtotal.
- Comparison operators create boolean values such as `quantity > 10`.
- Ternary expressions can choose between two values.
- `===` should be preferred over `==`.

## Ch4 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch4 Summary

- `if / else if / else` lets code choose between multiple conditions.
- `switch` starts at the matching case and needs `break` to stop.
- Truthy/falsy values let non-boolean values behave like conditions.
- `||` can be used to choose a fallback value.

## Ch5 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch5 Summary

- Functions help us reuse code.
- Parameters receive values from the caller.
- Arguments are the actual values we pass in.
- `return` sends a value back out of a function.
- Default parameters help when no argument is passed.

## Ch6 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch6 Summary

- Arrays store multiple values in order.
- Index starts at `0`.
- `.length` gives the number of items.
- `.push()` adds to the end.
- `.pop()` removes the last item.
- `for...of` loops through each item.

## Ch7 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch7 Summary

- `map()` transforms every item.
- `filter()` keeps items that match a condition.
- `find()` returns the first matching item.
- `some()` checks if at least one item matches.
- `every()` checks if all items match.
- `reduce()` combines many values into one result.

## Ch8 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch8 Summary

- Objects store data as `key: value` pairs.
- Dot notation is the most common way to read properties.
- Objects can also contain functions called methods.
- Destructuring pulls values out into variables.
- Spread helps create a new object from an existing one.

## Ch9 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch9 Summary

- A callback is a function passed into another function.
- A higher-order function takes or returns a function.
- A closure lets a function remember values from outside it.
- Rest parameters gather many arguments into one array.
- Spread can unpack an array into separate arguments.

## Ch10 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch10 Summary

- String methods help clean and transform text.
- Template literals make string formatting easier.
- Regex can check simple text patterns.
- `Date` helps us work with real dates and time values.
- `.toLocaleDateString()` is useful for human-readable date output.

## Ch11 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch11 Summary

- `try` contains code that may fail.
- `catch` handles errors so the whole program does not crash.
- `finally` always runs, whether success or failure happens.
- `return` from a function is different from `console.log()`.

## Ch12 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch12 Summary

- Async work does not finish immediately.
- `await` waits for a promise inside the current async function flow.
- `fetch()` gets data from a URL.
- We should await the async result before using array properties like `.length`.

## Ch13 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch13 Summary

- TypeScript is JavaScript with types.
- Type annotations can make code clearer and catch mistakes earlier.
- Type inference means TS can often guess types for us.
- We can start small by typing simple variables and function parameters.

## Ch14 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch14 Summary

- TypeScript can describe arrays, tuples, and unions.
- `type` and `interface` both describe data shapes.
- Optional properties use `?`.
- `readonly` protects values from reassignment.

## Ch15 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch15 Summary

- Function parameters and return values can be typed clearly.
- Function type aliases describe the shape of a function.
- Generics let one function work with many types safely.
- Utility types like `Pick` and `Omit` reshape existing types.

## Ch16 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch16 Summary

- Narrowing helps TypeScript understand a more specific type after checks.
- Type guards let us safely inspect `unknown` values.
- Discriminated unions make multi-shape data easier to handle.
- `unknown` is safer than `any` because it forces checks first.

## Ch17 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch17 Summary

- Node.js runs the backend server.
- Express helps define routes quickly.
- `req` is the incoming request.
- `res` is the outgoing response.
- `res.json()` is a common way to return API data.

## Ch18 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch18 Summary

- CRUD API maps well to `GET`, `POST`, `PUT`, and `DELETE`.
- `req.params` is used for path values like ids.
- `req.body` is used for incoming JSON data.
- `express.json()` is required before reading JSON body data.
- In-memory arrays are useful for learning API flow before databases.

## Ch19 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch19 Summary

- Middleware can stop bad requests before they reach route handlers.
- Validation should match the contract of each route.
- `POST` and `PUT` often need different validation rules.
- Consistent `{ message: ... }` error responses make APIs easier to use and debug.

## Ch20 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch20 Summary

- Backend code becomes easier to maintain when routes, middleware, data, and types are split by responsibility.
- `app.ts` should compose middleware and routers.
- `server.ts` should only start the app.
- A router should usually use paths relative to its mount point.

## Ch21 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch21 Summary

- JSON files are a simple first persistence layer before a real database.
- File storage works well when separated behind a storage layer.
- Async route handlers must await storage operations.
- Persistence is only useful if behavior still matches the API contract.

## Ch22 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch22 Summary

- Automated tests reduce manual API checking.
- Test data should be isolated from production data.
- Cleanup must close the server and restore fixtures reliably.
- Test runner lifecycle hooks are safer than time-based cleanup.

## Bridge 01 Checklist

- [x] Create bridge lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Bridge summary

## Bridge 01 Summary

- Promise represents a value that will arrive later.
- `await` converts `Promise<T>` flow into `T` flow inside an async function.
- Callback APIs often need to be wrapped before they can be awaited cleanly.
- Cleanup code should wait for real completion, not rely on time-based guesses.

## Bridge 02 Checklist

- [x] Create bridge lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Bridge summary

## Bridge 02 Summary

- SQL commands have different jobs: `SELECT`, `INSERT`, `UPDATE`, `DELETE`.
- `WHERE id = ?` helps target one row instead of touching everything.
- `SELECT *` is convenient for learning/debugging, but explicit columns are clearer in app code.
- `ORDER BY` makes list behavior predictable instead of relying on guessed row order.

## Bridge 03 Checklist

- [x] Create bridge lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Bridge summary

## Bridge 03 Summary

- `.exec()` is for setup SQL, not row reads.
- `.all()` returns arrays and can return `[]` when no rows match.
- `.get()` returns one row or `undefined`.
- `.run()` is for `INSERT`, `UPDATE`, and `DELETE`, and its result object contains useful metadata.
- `lastInsertRowid` helps identify newly created rows, while `changes` shows whether a write query affected anything.

## Bridge 04 Checklist

- [x] Create bridge lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Bridge summary

## Bridge 04 Summary

- `.get()` returning `undefined` is a normal not-found result, not a SQL failure.
- `.all()` returning `[]` is a normal empty result.
- SQL errors happen when the query or schema is broken.
- Backend code should treat not found as `404` and real SQL failures as `500`.

## Test Bridge Plan

- [x] Plan test bridge sequence
- [x] Test Bridge 01 - Assert basics
- [x] Test Bridge 02 - SQLite result tests
- [x] Test Bridge 03 - Storage function tests
- [x] Test Bridge 04 - API status tests

## Test Bridge 01 Checklist

- [x] Create bridge lesson
- [x] Create example
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Bridge summary

## Test Bridge 01 Summary

- `test(...)` defines one behavior-focused test case.
- `assert.equal(...)` is for primitive values like numbers, strings, and `undefined`.
- `assert.deepEqual(...)` is for arrays and objects.
- `assert.ok(...)` is for truthy conditions.

## Test Bridge 02 Checklist

- [x] Create bridge lesson
- [x] Create example
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Bridge summary

## Test Bridge 02 Summary

- SQLite result tests should check behavior of `.all()`, `.get()`, `lastInsertRowid`, and `changes`.
- Resetting table data before each test makes result counts and ids predictable.
- Database rows may need cleanup or field-by-field asserts depending on the returned object shape.
- Query-level tests are useful before moving up to storage-level behavior tests.

## Test Bridge 03 Checklist

- [x] Create bridge lesson
- [x] Create example
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Bridge summary

## Test Bridge 03 Summary

- Storage function tests focus on behavior of app-level functions instead of raw SQL driver methods.
- Resetting the SQLite table before each test keeps ids and row counts predictable.
- `findTaskById()` should be tested for both found and missing cases.
- `createTask()` and `deleteTask()` should prove both success flow and repeat/not-found behavior.

## Test Bridge 04 Checklist

- [x] Create bridge lesson
- [x] Create example
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Bridge summary

## Test Bridge 04 Summary

- API tests verify route behavior, status codes, and response bodies through real HTTP requests.
- `after()` is the safe place to close the test server so the process does not hang.
- Even HTTP-level tests still need controlled database state to stay predictable.
- `400` and `404` are different failures and should be tested separately.

## Ch23 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch23 Summary

- SQLite stores data in a local file and is useful as a first real database.
- A table schema defines the shape of stored rows.
- Database rows often need mapping before they match app-level types.
- `0/1` values in SQLite often need conversion into booleans in the app.

## Ch24 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] SQL revision after bridge
- [x] Chapter summary

## Ch24 Summary

- SQLite can replace JSON storage without changing the outer API contract.
- Database rows often need mapping before they match app-level types.
- `lastInsertRowid` and `changes` are useful for create/delete flows.
- The route layer should keep focusing on request/response behavior while storage handles persistence.

## Ch25 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch25 Summary

- `db.ts` should own database connection and setup.
- Query functions become easier to read when grouped in one dedicated file.
- Routes become cleaner when they focus only on HTTP behavior.
- Internal refactors are safer when API behavior stays stable.

## Ch26 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [x] Student completes exercise
- [x] Review exercise
- [x] Chapter summary

## Ch26 Summary

- A test database should be separate from the app's normal database.
- Test setup should control table state with reset and seed helpers.
- API tests should verify both HTTP status and the returned body shape.
- Cleanup should close the server after the run to avoid hanging test processes.

## Ch27 Checklist

- [x] Create chapter lesson
- [x] Create examples
- [x] Create guided exercise
- [ ] Student completes exercise
- [ ] Review exercise
- [ ] Chapter summary

## Current Exercise

- File: `exercises/ch27-task-api-timestamps/`
- Task:
  - add `created_at` and `updated_at` to the SQLite schema
  - map timestamp fields from DB rows into app-level task objects
  - return timestamp fields from create/read/update responses
  - update `updated_at` when a task changes

## Review Rules

- First say what is good.
- Then give max 3 feedback points.
- If it runs and meets the requirement, pass it.
- Style polish can wait unless it blocks understanding.
