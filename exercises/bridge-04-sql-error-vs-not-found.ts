import path from "node:path";
import { DatabaseSync } from "node:sqlite";

const dbPath = path.join(__dirname, "bridge-04-storage/tasks.db");
const db = new DatabaseSync(dbPath);

db.exec(`
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL DEFAULT 0
  )
`);

// TODO 1:
db.prepare("DELETE FROM tasks").run();
// TODO 2:
db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run("Study SQL", 0);
const insertResult  = db.prepare("INSERT INTO tasks (title, done) VALUES (?, ?)").run("Build API", 1);

// TODO 3:
const foundTask = db.prepare("SELECT * FROM tasks WHERE id = ?").get(insertResult .lastInsertRowid)

// TODO 4:
const missingTask = db.prepare("SELECT * FROM tasks WHERE id = ?").get(9999)

// TODO 5:
const emptyRows = db.prepare("SELECT * FROM tasks WHERE done = ?").all(2)

// TODO 6:
let queryStatus: string | undefined = undefined
try {
  const brokenQuery = db
    .prepare("SELECT id, title, done FROM wrong_table WHERE id = ?")
    .get(1);
    
  console.log(brokenQuery);
} catch (err){
  queryStatus = "sql error"
  console.log(err);
}

// TODO 7:
// พิมพ์:
console.log("foundTask:", foundTask);
console.log("missingTask:", missingTask);
console.log("emptyRows:", emptyRows);
console.log("queryStatus:", queryStatus);

// TODO 8:
// ตอบเป็นคอมเมนต์สั้น ๆ:
// - why missingTask is not a SQL error : missingTask ยังทำงานถูกต้องของมันไม่ได้ผิดอะไรเลยไม่ Error 
// - why emptyRows is not a SQL error : emptyRows มันหาค่านั้นๆไม่เจอเลยคือ Empty Rows
// - how SQL throw is different from not found : มันช่วยให้ Debug ได้ง่ายขึ้น
// - how backend should think differently about 404 and 500 : 404 คือ Error Not Found แต่ 500 คือ Server Error คนละ Error Code คนละความหมาย
