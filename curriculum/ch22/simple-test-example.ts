import test from "node:test";
import assert from "node:assert/strict";

test("array length should be 2", () => {
  const items = ["a", "b"];
  assert.equal(items.length, 2);
});
