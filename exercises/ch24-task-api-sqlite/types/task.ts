type Task = {
  id: number;
  title: string;
  done: boolean;
};

interface RawTask {
  id: number;
  title: string;
  done: number; 
}

export { Task, RawTask }