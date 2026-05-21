import { createServer } from "node:http";

const server = createServer((req, res) => {
  res.end("ok");
});

server.listen(3001, () => {
  console.log("runing on port 3001");
});

const getTaskTitles = async (): Promise<string[]> => {
  // string[] คือ arry ที่ด้านในเป็น String
  return await new Promise<string[]>((resolve) => {
    resolve(["Title 1", "Title 2"]);
  });
};

const closeServer = async (): Promise<void> => {
  // Void คือ func ที่ไม่ Return อะไรกลับไป
  await new Promise<void>((resolve, reject) => {
    server.close((error) => {
      if (error) reject(error);
      else resolve();
    });
  });
};

const wait = (ws: number) => {
  return new Promise<string>((resolve) => {
    // String คือ String ตัวเดียว
    setTimeout(() => {
      resolve("done");
    }, ws);
  });
};

const runDemo = async () => {
  const waiting = await wait(35);
  console.log(waiting);
  const GetTitile = await getTaskTitles();
  console.log(GetTitile);

  closeServer();
};

runDemo();
