const safeParse = (text) => {
  // TODO: คืน { ok: true, value } เมื่อ parse สำเร็จ
  // TODO: คืน { ok: false, error: 'Invalid JSON' } เมื่อ parse ไม่สำเร็จ
};

const isValidTask = (value) => {
  // TODO: value ต้องเป็น object ที่ไม่ใช่ null
  // TODO: title ต้องเป็น string ที่ไม่ว่างหลัง trim()
  // TODO: done ถ้ามี ต้องเป็น boolean
};

const parseTaskList = (text) => {
  // TODO: ใช้ safeParse ก่อน
  // TODO: ต้องเป็น array และทุก item ผ่าน isValidTask
  // TODO: คืน { ok, value } หรือ { ok: false, error: 'Invalid task list' }
};

const toId = (value) => {
  // TODO: คืน integer ที่มากกว่า 0 หรือ null
};

console.log('valid list:', parseTaskList('[{"id":1,"title":"Learn JS","done":false}]'));
console.log('broken json:', parseTaskList('{ bad json }'));
console.log('bad item:', parseTaskList('[{"id":1,"title":""}]'));
console.log('id ok:', toId('12'));
console.log('id bad:', toId('abc'));
