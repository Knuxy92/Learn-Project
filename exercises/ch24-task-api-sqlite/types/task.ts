type Task = {
  id: number;
  title: string;
  done: boolean;
};

type DbTaskRow = {
  id: number;
  title: string;
  done: number;
};

export { type Task, type DbTaskRow };
