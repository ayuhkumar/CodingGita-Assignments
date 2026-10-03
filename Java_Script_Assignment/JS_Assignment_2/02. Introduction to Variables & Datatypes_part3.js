
// PART H - Non-Primitive Data Types Basic Creation & Usage



// 1. Create an Object


let student = {
    name: "Riya",
    age: 18,
    isEnrolled: true
};

console.log(student);
console.log(student.name);
console.log(student.age);
console.log(student.isEnrolled);

// Output:
// { name: 'Riya', age: 18, isEnrolled: true }
// Riya
// 18
// true



// 2. Work with Arrays


let scores = [85, 92, 78, 90];
let mixedData = [25, "Hello", true, null];

console.log(scores);
console.log(mixedData);
console.log(scores[0]);
console.log(scores[3]);

// Output:
// [85, 92, 78, 90]
// [25, 'Hello', true, null]
// 85
// 90



// 3. Declare and Call a Function


function calculateArea(length, width) {
    return length * width;
}

console.log(calculateArea(10, 5));
console.log(calculateArea(8, 4));

// Output:
// 50
// 32



// 4. Check Types with typeof

let numberValue = 25;
let stringValue = "Hello";
let booleanValue = true;
let nullValue = null;
let objectValue = { name: "Riya" };
let arrayValue = [10, 20, 30];
let functionValue = function() {
    return "Hello";
};

console.log(numberValue, typeof numberValue);
console.log(stringValue, typeof stringValue);
console.log(booleanValue, typeof booleanValue);
console.log(nullValue, typeof nullValue);
console.log(objectValue, typeof objectValue);
console.log(arrayValue, typeof arrayValue);
console.log(functionValue, typeof functionValue);

// Output:
// 25 number
// Hello string
// true boolean
// null object
// { name: 'Riya' } object
// [10, 20, 30] object
// [Function: functionValue] function

// Observation:
// typeof null returns "object" because of a historical JavaScript behavior.
// typeof an array also returns "object".




// PART I - Naming Rules & Best Practices



// 5. Valid vs Invalid Variable Names


// Valid:
// userName
// _privateData
// $price
// totalCount

// Invalid:
// 2ndPlace
// Reason: A variable name cannot start with a number.

// my-age
// Reason: Hyphen (-) is not allowed in variable names.

// function
// Reason: function is a reserved JavaScript keyword.

// const
// Reason: const is a reserved JavaScript keyword.

// Correct examples:

let userName;
let _privateData;
let $price;
let totalCount;



// 6. Apply Best Practices


const length = 10;
const width = 5;
const area = length * width;
const MAX_VALUE = 100;

console.log(length);
console.log(width);
console.log(area);
console.log(MAX_VALUE);

// Output:
// 10
// 5
// 50
// 100



// 7. Declaration & Assignment

let studentAge;

studentAge = 18;

let studentName = "Ayush";

const country = "India";

console.log(studentAge);
console.log(studentName);
console.log(country);

// Output:
// 18
// Ayush
// India




// PART J - Prediction & Fixing



// 8. Predict the Output


let person = {
    name: "Amit",
    age: 22
};

let colors = ["red", "green", "blue"];

function sayHi() {
    return "Hi!";
}

let empty = null;

console.log(typeof person);
console.log(typeof colors);
console.log(typeof sayHi);
console.log(typeof empty);
console.log(person.name);
console.log(colors[1]);
console.log(sayHi());

// Output:
// object
// object
// function
// object
// Amit
// green
// Hi!

// Explanation:
// Objects have the typeof result "object".
// Arrays also have the typeof result "object".
// Functions have the typeof result "function".
// typeof null returns "object" because of a historical JavaScript behavior.



// 9. Fix the Program



let student1 = {
    name: "Neha",
    age: 19
};


let scores2 = [90, 85, 88];

function greet(name) {
    return "Hello " + name;
}


let maxScore = 100;
maxScore = 95;

console.log(student1.name);
console.log(scores2[0]);
console.log(greet("Neha"));
console.log(maxScore);

// Output:
// Neha
// 90
// Hello Neha
// 95



// 10. Concept Questions
// a)
// Object example:
let personData = {
    name: "Ayush",
    age: 18
};


let subjectMarks = [80, 75, 90];



// b)

// Answer:
// typeof null returns "object" because of a historical behavior
// in JavaScript.
// However, null is not actually an object.
// It represents an intentional empty or missing value.



// c)

// Answer:
// Keeping the same type of data in an array makes the code easier
// to understand, maintain, and process.
// It also makes operations on the array more predictable.

let marks = [80, 85, 90, 95];



// d)

// Answer:
// Use const when the variable should not be re-assigned.
// Use let when the variable needs to be re-assigned.


const collegeName = "ABC College";


let marksObtained = 80;
marksObtained = 90;

// Output:
// collegeName = ABC College
// marksObtained = 90