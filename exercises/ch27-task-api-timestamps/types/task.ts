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

export { type Task, type DbTaskRow };
