// // Part-D JavaScript Reverse For Loop

// // Q1.
// for (let i = 50; i >= 1; i--) {
//     if (i % 3 === 0 && i % 9 !== 0) {
//         console.log(i);
//     }
// }

// // Q2.
// let num = 4729;
// let product = 1;

// for (; num > 0; num = Math.floor(num / 10)) {
//     let digit = num % 10;

//     if (digit % 2 !== 0) {
//         product *= digit;
//     }
// }

// console.log(product);
// // Output: 63

// // Q3.
// let text = "Programming";
// let consonants = "";

// for (let i = text.length - 1; i >= 0; i--) {
//     let ch = text[i].toLowerCase();

//     if (ch !== "a" && ch !== "e" && ch !== "i" &&
//         ch !== "o" && ch !== "u") {
//         consonants += text[i];
//     }
// }

// console.log(consonants);
// // Output: gnimrgorP

// // Q4.
// let first = 0;
// let second = 1;
// let fib = "";
// let count = 0;

// for (let i = 1; i <= 15; i++) {
//     fib += first + " ";
//     let next = first + second;
//     first = second;
//     second = next;
//     count++;
// }

// let fibArray = fib.trim().split(" ");

// for (let i = fibArray.length - 1; i >= 0; i--) {
//     console.log(fibArray[i]);
// }
// // Output: First 15 Fibonacci numbers in reverse order

// // Q5.
// let number = 12321;
// let original = number;
// let reversed = 0;

// for (; number > 0; number = Math.floor(number / 10)) {
//     let digit = number % 10;
//     reversed = reversed * 10 + digit;
// }

// if (original === reversed) {
//     console.log("Palindrome");
// } else {
//     console.log("Not a Palindrome");
// }
// // Output: Palindrome

// // Q6.
// let numbers = [12, 45, 7, 23, 56, 89, 34];
// let largest = -Infinity;

// for (let i = numbers.length - 1; i >= 0; i--) {
//     if (numbers[i] < 50 && numbers[i] > largest) {
//         largest = numbers[i];
//     }
// }

// console.log(largest);
// // Output: 45

// // Q7.
// let temperatures = [32, 28, 41, 19, 35, 27, 38];
// let coldDays = 0;

// for (let i = temperatures.length - 1; i >= 0; i--) {
//     if (temperatures[i] < 30) {
//         coldDays++;
//     }
// }

// console.log(coldDays);
// // Output: 3

// // Q8.
// let decimal = 13;
// let binary = "";

// if (decimal === 0) {
//     binary = "0";
// } else {
//     for (; decimal > 0; decimal = Math.floor(decimal / 2)) {
//         binary += decimal % 2;
//     }
// }

// console.log(binary);
// // Output: 1011

// // Q9.
// let scores = [90, 85, 70, 95, 60, 88, 75];

// for (let i = scores.length - 1; i >= 0; i--) {
//     if (scores[i] > 80) {
//         console.log("Score:", scores[i]);
//         console.log("Index:", i);
//         break;
//     }
// }
// // Output: Score: 88
// // Output: Index: 5

// // Q10.
// for (let i = 40; i >= 1; i--) {
//     let root = Math.sqrt(i);

//     if (Number.isInteger(root)) {
//         continue;
//     }

//     console.log(i);
// }
// // Output: Numbers from 40 down to 1, excluding perfect squares