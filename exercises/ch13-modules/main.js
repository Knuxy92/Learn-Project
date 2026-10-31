import { add, multiply } from './calculator.js';
import formatResult from './formatter.js';

// TODO: พิมพ์ผลบวกของ 2 กับ 3 ด้วย formatResult
console.log(formatResult('Sum', add(2, 3)));

// TODO: พิมพ์ผลคูณของ 4 กับ 5 ด้วย formatResult
console.log(formatResult('Product', multiply(4, 5)));
