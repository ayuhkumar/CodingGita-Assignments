// //Part - C
// //Part C-a - break inside a for Loop

// // Q1. 
// let values = [2, 5, 7, 9, 7];

// for (let i = 0; i < values.length; i++) {
//     if (values[i] === 7) {
//         console.log("Index:", i);
//         break;
//     }
// }
// // Output: Index: 2

// // Q2. 
// let correctPassword = "admin123";
// let enteredPassword = "admin123";
// let accessGranted = false;

// for (let attempt = 1; attempt <= 5; attempt++) {
//     if (enteredPassword === correctPassword) {
//         console.log("Access granted");
//         accessGranted = true;
//         break;
//     }
// }

// if (!accessGranted) {
//     console.log("Account locked");
// }
// // Output: Access granted
// // Note: This uses a fixed value to simulate input.

// // Q3. 
// let sum1 = 0;
// let lastNumber = 0;

// for (let i = 1; ; i++) {
//     sum1 += i;

//     if (sum1 > 100) {
//         lastNumber = i;
//         console.log("Last number added:", lastNumber);
//         break;
//     }
// }
// // Output: Last number added: 14

// // Q4.
// let names = ["Rahul", "Aman", "Sneha", "Sam"];

// for (let i = 0; i < names.length; i++) {
//     if (names[i][0] === "S") {
//         console.log(names[i]);
//         break;
//     }
// }
// // Output: Sneha

// // Q5.
// for (let i = 1; i <= 50; i++) {
//     if (i > 20 && Number.isInteger(Math.sqrt(i))) {
//         console.log("Stopped at:", i);
//         break;
//     }
// }
// // Output: Stopped at: 25


// //Part C-b - continue inside a for Loop

// // Q1. 
// for (let i = 1; i <= 30; i++) {
//     if (i % 4 === 0) {
//         continue;
//     }
//     console.log(i);
// }
// // Output: Numbers from 1 to 30, excluding multiples of 4

// // Q2. 
// let mixedNumbers = [5, -3, 10, -2, 7, -8];
// let positiveSum = 0;

// for (let i = 0; i < mixedNumbers.length; i++) {
//     if (mixedNumbers[i] <= 0) {
//         continue;
//     }
//     positiveSum += mixedNumbers[i];
// }

// console.log("Positive sum:", positiveSum);
// // Output: Positive sum: 22

// // Q3. 
// let message = "Hello World";

// for (let i = 0; i < message.length; i++) {
//     if (message[i] === " ") {
//         continue;
//     }
//     console.log(message[i]);
// }
// // Output: H e l l o W o r l d (each character on a new line)

// // Q4. 
// for (let i = 1; i <= 12; i++) {
//     let product = 6 * i;

//     if (product % 5 === 0) {
//         continue;
//     }

//     console.log("6 x " + i + " = " + product);
// }
// // Output: All rows from 6 x 1 to 6 x 12, excluding products divisible by 5

// // Q5. 
// let ages = [12, 18, 25, 15, 30, 17, 22];

// for (let i = 0; i < ages.length; i++) {
//     if (ages[i] < 18) {
//         continue;
//     }
//     console.log(ages[i]);
// }
// // Output: 18, 25, 30, 22