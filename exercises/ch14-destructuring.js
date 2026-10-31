const task = {
  id: 1,
  title: 'Learn JS',
  done: false,
  meta: { priority: 'high', tags: ['js'] },
};

const describeTask = (task) => {
  // TODO: destructure title, done, และ priority (default 'normal')
  // TODO: คืน string `title - done|pending - priority`
};

const updateTask = (task, updates) => {
  // TODO: คืน object ใหม่ที่รวม updates โดยไม่แก้ task เดิม
};

const splitTask = (task) => {
  // TODO: แยก id ออก แล้วคืน { id, rest }
};

console.log('describeTask:', describeTask(task));
console.log('updateTask:', updateTask(task, { done: true }));
console.log('splitTask:', splitTask(task));
