import { readFile, writeFile } from "node:fs/promises";

const filePath = "./storage/example.json";

const readItems = async (): Promise<unknown> => {
  const raw = await readFile(filePath, "utf-8");
  return JSON.parse(raw);
};

const writeItems = async (items: unknown): Promise<void> => {
  await writeFile(filePath, JSON.stringify(items, null, 2));
};

export { readItems, writeItems };
