import { access, mkdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';

const dataDir = path.join(import.meta.dirname, 'ch15-data');
const filePath = path.join(dataDir, 'note.json');

const noteExists = async () => {
  // TODO: ใช้ access ตรวจว่าไฟล์มีอยู่ คืน true หรือ false
};

const saveNote = async (text) => {
  // TODO: สร้าง { text, savedAt } แล้วเขียนลงไฟล์เป็น JSON
  // TODO: ต้อง mkdir dataDir ก่อนเขียน
};

const loadNote = async () => {
  // TODO: อ่านไฟล์แล้ว JSON.parse คืน object
};

const run = async () => {
  const exists = await noteExists();
  console.log('note exists:', exists);

  if (exists === false) {
    await saveNote('first note');
  }

  const note = await loadNote();

  if (note === undefined) {
    console.log('note text: ยังไม่ได้ทำ loadNote()');
    return;
  }

  console.log('note text:', note.text);
};

run();
