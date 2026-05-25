type DbTaskRow = {
  id: number;
  title: string;
  done: number;
  created_at: string;
  updated_at: string;
};

type Task = {
  id: number;
  title: string;
  done: boolean;
  createdAt: string;
  updatedAt: string;
};

const mapTaskRow = (row: DbTaskRow): Task => {
  return {
    id: row.id,
    title: row.title,
    done: row.done === 1,
    createdAt: row.created_at,
    updatedAt: row.updated_at,
  };
};

const sampleRow: DbTaskRow = {
  id: 1,
  title: "Add timestamps",
  done: 0,
  created_at: "2026-05-22 10:00:00",
  updated_at: "2026-05-22 10:00:00",
};

console.log(mapTaskRow(sampleRow));
