// //  JavaScript for Loop

// //  Part B - Additional Advanced Questions

// // Q1. 
// let temperatures = [28, 32, 25, 40, 18, 35];
// let hotDays = 0;

// for (let i = 0; i < temperatures.length; i++) {
//     if (temperatures[i] > 30) {
//         hotDays++;
//     }
// }
// console.log("Hot days:", hotDays);
// // Output: Hot days: 3

// // Q2. 
// let number = 4729;
// let sum = 0;

// for (; number > 0; number = Math.floor(number / 10)) {
//     sum += number % 10;
// }
// console.log("Sum of digits:", sum);
// // Output: Sum of digits: 22

// // Q3. 
// for (let i = 1; i <= 100; i++) {
//     if (i % 3 === 0 && i % 5 === 0 && i % 7 !== 0) {
//         console.log(i);
//     }
// }
// // Output: 15, 30, 45, 60, 90

// // Q4. 
// let text = "JavaScript";
// let consonants = "";

// for (let i = 0; i < text.length; i++) {
//     let ch = text[i].toLowerCase();

//     if (ch !== "a" && ch !== "e" && ch !== "i" &&
//         ch !== "o" && ch !== "u") {
//         consonants += text[i];
//     }
// }
// console.log(consonants);
// // Output: JvScrpt

// // Q5. 
// let numbers = [12, 45, 23, 89, 34];
// let largest = numbers[0];

// for (let i = 1; i < numbers.length; i++) {
//     if (numbers[i] > largest) {
//         largest = numbers[i];
//     }
// }
// console.log("Largest number:", largest);
// // Output: Largest number: 89

// // Q6. 
// let num = 28;
// let divisorSum = 0;

// for (let i = 1; i < num; i++) {
//     if (num % i === 0) {
//         divisorSum += i;
//     }
// }

// if (divisorSum === num) {
//     console.log("Perfect Number");
// } else {
//     console.log("Not a Perfect Number");
// }
// // Output: Perfect Number

// // Q7. 
// let value = 1;

// for (let i = 1; i <= 8; i++) {
//     console.log(value);
//     value *= 2;
// }
// // Output: 1 2 4 8 16 32 64 128

// // Q8. 
// let first = 0;
// let second = 1;

// for (let i = 1; i <= 20; i++) {
//     console.log(first);
//     let next = first + second;
//     first = second;
//     second = next;
// }
// // Output: First 20 Fibonacci numbers, starting with 0 and 1

// // Q9.
// let scores = [45, 78, 90, 32, 56, 88];
// let total = 0;

// for (let i = 0; i < scores.length; i++) {
//     total += scores[i];
// }

// let average = total / scores.length;
// let aboveAverage = 0;

// for (let i = 0; i < scores.length; i++) {
//     if (scores[i] > average) {
//         aboveAverage++;
//     }
// }

// console.log("Average:", average);
// console.log("Students above average:", aboveAverage);
// // Output: Average: 64.83333333333333
// // Output: Students above average: 3

// // Q10. 
// let decimal = 13;
// let binary = "";

// if (decimal === 0) {
//     binary = "0";
// } else {
//     for (; decimal > 0; decimal = Math.floor(decimal / 2)) {
//         binary = (decimal % 2) + binary;
//     }
// }
// console.log("Binary:", binary);
// // Output: Binary: 1101


