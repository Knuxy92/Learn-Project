import { readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';

const filePath = path.join(import.meta.dirname, 'storage', 'example.json');

const readItems = async () => {
  const raw = await readFile(filePath, 'utf-8');

  return JSON.parse(raw);
};

const writeItems = async (items) => {
  await writeFile(filePath, JSON.stringify(items, null, 2));
};

export { readItems, writeItems };
