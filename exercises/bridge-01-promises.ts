import { resolve } from "node:dns";
import { createServer } from "node:http";

const server = createServer((req, res) => {
  res.end("ok");
});

server.listen(3001, () => {
  console.log("runing on port 3001");
});

const wait = async (ms: number): Promise<string> => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve("done");
    }, ms);
  })
};

const getTaskTitles = async (): Promise<string[]> => {
  return new Promise((resolve) => {
    resolve(["Title 1", "Title 2"])
  });
};

const closeServer = async (server: ReturnType<typeof createServer>): Promise<void> => {
  await new Promise<void>((resolve, reject) => {
    server.close((error) => {
      if (error) reject(error);
      else resolve();
    });
  });
};

const runDemo = async (): Promise<void> => {
  const waiting = await wait(35);
  console.log(waiting);

  const taskTitles = await getTaskTitles();
  console.log(`Task count: ${taskTitles.length}`);

  await closeServer(server);
};



// TODO:
// - Promise ที่ตอบกลับด้วย Arry String จะรอจนกว่าจะ resolve ถึงจะคืนคำตอบ
// - Arry String ธรรมดา

runDemo();
export { wait, getTaskTitles, closeServer, runDemo };
