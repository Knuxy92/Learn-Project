type Book = {
  title: string;
  pages: number;
};

interface Author {
  name: string;
  age: number;
}

const book: Book = {
  title: 'TypeScript Basics',
  pages: 120,
};

const author: Author = {
  name: 'Neo',
  age: 20,
};

console.log(book);
console.log(author);
