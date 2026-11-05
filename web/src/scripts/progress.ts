/* เก็บความคืบหน้าผู้เรียน — localStorage ทั้งหมด (ไม่มี server)
   lp:teaching · lp:last · lp:done:{chNN} */

const KEY_TEACH = "lp:teaching";
const KEY_LAST = "lp:last";
const keyDone = (ch: string) => `lp:done:${ch}`;

export const getTeaching = (): boolean => localStorage.getItem(KEY_TEACH) !== "0";
export const setTeaching = (on: boolean): void => {
  localStorage.setItem(KEY_TEACH, on ? "1" : "0");
};

export const setLastChapter = (ch: string): void => {
  localStorage.setItem(KEY_LAST, ch);
};
export const getLastChapter = (): string | null => localStorage.getItem(KEY_LAST);

const readDone = (ch: string): string[] => {
  try {
    const raw = localStorage.getItem(keyDone(ch));
    const list = raw ? (JSON.parse(raw) as unknown) : [];
    return Array.isArray(list) ? list.filter((x): x is string => typeof x === "string") : [];
  } catch {
    return [];
  }
};

const writeDone = (ch: string, list: string[]): void => {
  localStorage.setItem(keyDone(ch), JSON.stringify(list));
};

export function initTasks(): void {
  const ch = document.documentElement.dataset.ch;
  if (!ch) return;
  // หมายเลขโจทย์ผูกกับลำดับใน DOM (นิ่งตามเนื้อหา) ไม่พึ่งค่าจาก build
  const boxes = [...document.querySelectorAll<HTMLInputElement>("input[data-task]")];
  boxes.forEach((box, idx) => {
    box.dataset.task = String(idx + 1);
    if (readDone(ch).includes(String(idx + 1))) box.checked = true;
  });
  document.addEventListener("change", (e) => {
    const input = e.target as HTMLElement | null;
    if (!input || !(input instanceof HTMLInputElement) || !input.dataset.task) return;
    const now = boxes.filter((box) => box.checked).map((box) => box.dataset.task!);
    writeDone(ch, now);
  });
}

interface ChapterMeta {
  no: number;
  title: string;
}

export function initResume(): void {
  const line = document.getElementById("resume-line");
  if (!line) return;
  const last = getLastChapter();
  if (!last) return;
  let map: Record<string, ChapterMeta> = {};
  try {
    map = JSON.parse(line.dataset.chapters ?? "{}") as Record<string, ChapterMeta>;
  } catch {
    return;
  }
  const meta = map[last];
  if (!meta) return;
  const a = document.createElement("a");
  a.href = `/chapters/${last}/`;
  a.textContent = `บทที่ ${String(meta.no).padStart(2, "0")} · ${meta.title}`;
  line.textContent = "อ่านค้างไว้ที่ ";
  line.appendChild(a);
  line.hidden = false;
}
