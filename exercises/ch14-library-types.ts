type Book = {
  readonly id: number;
  title: string;
  pages: number;
  genre: "fiction" | "non-fiction";
  authorName?: string;
};

interface Library {
  name: string;
  books: Book[];
}

const newbook: Book = {
  id: 10,
  title: "test",
  pages: 120,
  genre: "non-fiction"
};

const featuredBook: [string, number] = [newbook.title, newbook.pages];
const bookId: string | number = newbook.id;

const library: Library = {
  name: "Lib1",
  books: [newbook],
};

console.log(featuredBook);
console.log(bookId);
console.log(library);
