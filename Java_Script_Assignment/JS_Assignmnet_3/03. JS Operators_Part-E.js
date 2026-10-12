// //  Increment / Decrement Operators (++ / --)

// //  Part A - Basic Increment and Decrement

// // Q1.
// let counter = 5;
// counter++;
// console.log(counter); // Output: 6

// // Q2.
// let lives = 3;
// lives--;
// console.log(lives); // Output: 2

// // Q3.
// let score = 10;
// score++;
// console.log(score); // Output: 11

// // Q4.
// let items = 8;
// items--;
// console.log(items); // Output: 7

// // Q5.
// let count = 0;
// count++;
// count++;
// console.log(count); // Output: 2


// //Part B - Pre-increment and Post-increment

// // Q6.
// let x = 5;
// let y = x++;
// console.log(x, y); // Output: 6 5
// // Explanation: x++ uses the old value first, then increments x.

// // Q7.
// let a = 5;
// let b = ++a;
// console.log(a, b); // Output: 6 6
// // Explanation: ++a increments a first, then uses the new value.

// // Q8.
// let previousLives = 3;
// let oldLives = previousLives--;
// console.log(previousLives, oldLives); // Output: 2 3
// // Explanation: Post-decrement stores the old value first.

// // Q9.
// let attempts = 0;
// let currentAttempts = ++attempts;
// console.log(attempts, currentAttempts); // Output: 1 1
// // Explanation: Pre-increment increases the value before storing it.

// // Q10.
// let points = 100;
// points++;
// points--;
// console.log(points); // Output: 100


// // Part C - Predict the Output

// // Q11.
// let x1 = 10;
// let y1 = x1++;
// let z1 = ++x1;
// console.log(x1, y1, z1); // Output: 12 10 12
// // Explanation: Post-increment uses the old value; pre-increment uses the new value.

// // Q12.
// let a1 = 5;
// let b1 = a1-- + ++a1;
// console.log(a1, b1); // Output: 5 10
// // Explanation: a1-- gives 5, then ++a1 returns it to 5.

// // Q13.
// let m = 7;
// let n = --m + m++;
// console.log(m, n); // Output: 7 13
// // Explanation: --m gives 6, and m++ gives 6 before increasing m.

// // Q14.
// let p = 3;
// let q = p++ + ++p + p;
// console.log(p, q); // Output: 5 13
// // Explanation: The values added are 3 + 5 + 5.

// // Q15.
// let val = 0;
// val = val++ + ++val;
// console.log(val); // Output: 2
// // Explanation: val++ gives 0, then ++val gives 2. Their sum is 2.