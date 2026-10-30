const studentName = "Student";
const score = 85;

let grade = "";
let gradeMessage = "";

const displayName = studentName || "Anonymous student";

if (score >= 90) {
  grade = "A";
} else if (score >= 80) {
  grade = "B";
} else if (score >= 70) {
  grade = "C";
} else if (score >= 60) {
  grade = "D";
} else {
  grade = "F";
}

switch (grade) {
  case "A":
    gradeMessage = "Excellent work";
    break;
  case "B":
    gradeMessage = "Great job";
    break;
  case "C":
    gradeMessage = "Good effort";
    break;
  case "D":
    gradeMessage = "Needs improvement";
    break;
  default:
    gradeMessage = "Keep practicing";
}

console.log(`Student: ${displayName}`);
console.log(`Score: ${score}`);
console.log(`Grade: ${grade}`);
console.log(`Message: ${gradeMessage}`);
