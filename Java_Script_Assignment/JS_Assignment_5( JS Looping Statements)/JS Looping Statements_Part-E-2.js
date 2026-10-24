// //  JavaScript While Loop

// // Q1. Print Numbers
// let i = 1;

// while (i <= 10) {
//     console.log(i);
//     i++;
// }

// // Q2. Sum of Natural Numbers
// let num1 = 1;
// let sum1 = 0;

// while (num1 <= 10) {
//     sum1 += num1;
//     num1++;
// }

// console.log(sum1);
// // Output: 55

// // Q3. Multiplication Table
// let table = 5;
// let j = 1;

// while (j <= 10) {
//     console.log(table + " x " + j + " = " + (table * j));
//     j++;
// }

// // Q4. Count the Digits
// let num2 = 58372;
// let count = 0;

// while (num2 > 0) {
//     count++;
//     num2 = Math.floor(num2 / 10);
// }

// console.log(count);
// // Output: 5

// // Q5. Reverse a Number
// let num3 = 12345;
// let reversed = 0;

// while (num3 > 0) {
//     let digit = num3 % 10;
//     reversed = reversed * 10 + digit;
//     num3 = Math.floor(num3 / 10);
// }

// console.log(reversed);
// // Output: 54321

// // Q6. Sum of Digits
// let num4 = 4729;
// let sum2 = 0;

// while (num4 > 0) {
//     sum2 += num4 % 10;
//     num4 = Math.floor(num4 / 10);
// }

// console.log(sum2);
// // Output: 22

// // Q7. Print Numbers with Conditions
// let num5 = 1;

// while (num5 <= 100) {
//     if (num5 % 3 === 0 && num5 % 5 === 0 && num5 % 7 !== 0) {
//         console.log(num5);
//     }
//     num5++;
// }
// // Output: 15, 30, 45, 60, 90

// // Q8. Calculate Factorial
// let num6 = 5;
// let factorial = 1;

// while (num6 > 1) {
//     factorial *= num6;
//     num6--;
// }

// console.log(factorial);
// // Output: 120

// // Q9. Check a Palindrome Number
// let num7 = 121;
// let original = num7;
// let reverse = 0;

// while (num7 > 0) {
//     let digit = num7 % 10;
//     reverse = reverse * 10 + digit;
//     num7 = Math.floor(num7 / 10);
// }

// if (original === reverse) {
//     console.log("Palindrome number");
// } else {
//     console.log("Not a Palindrome number");
// }
// // Output: Palindrome number

// // Q10. Convert Decimal to Binary
// let decimal = 13;
// let binary = "";

// while (decimal > 0) {
//     binary = (decimal % 2) + binary;
//     decimal = Math.floor(decimal / 2);
// }

// console.log(binary);
// // Output: 1101


// // JavaScript Do-While Loop

// // Q1. Print Numbers in Reverse
// let n1 = 10;

// do {
//     console.log(n1);
//     n1--;
// } while (n1 >= 1);

// // Q2. Print Even Numbers
// let n2 = 2;

// do {
//     console.log(n2);
//     n2 += 2;
// } while (n2 <= 20);

// // Q3. Sum of Natural Numbers
// let n3 = 5;
// let current = 1;
// let sum3 = 0;

// do {
//     sum3 += current;
//     current++;
// } while (current <= n3);

// console.log(sum3);
// // Output: 15

// // Q4. Product of Digits
// let n4 = 234;
// let product = 1;

// do {
//     product *= n4 % 10;
//     n4 = Math.floor(n4 / 10);
// } while (n4 > 0);

// console.log(product);
// // Output: 24

// // Q5. Find the First Digit
// let n5 = 58372;

// do {
//     if (n5 < 10) {
//         break;
//     }
//     n5 = Math.floor(n5 / 10);
// } while (n5 > 0);

// console.log(n5);
// // Output: 5

// // Q6. Calculate a Power
// let base = 3;
// let exponent = 4;
// let result = 1;
// let counter = 1;

// do {
//     result *= base;
//     counter++;
// } while (counter <= exponent);

// console.log(result);
// // Output: 81

// // Q7. Print Multiples with Conditions
// let n6 = 1;

// do {
//     if (n6 % 4 === 0 && n6 % 8 !== 0) {
//         console.log(n6);
//     }
//     n6++;
// } while (n6 <= 100);
// // Output: 4, 12, 20, 28, 36, 44, 52, 60, 68, 76, 84, 92, 100

// // Q8. Check a Palindrome Number
// let n7 = 1221;
// let original2 = n7;
// let reverse2 = 0;

// do {
//     reverse2 = reverse2 * 10 + (n7 % 10);
//     n7 = Math.floor(n7 / 10);
// } while (n7 > 0);

// if (original2 === reverse2) {
//     console.log("Palindrome number");
// } else {
//     console.log("Not a Palindrome number");
// }
// // Output: Palindrome number

// // Q9. Find the Greatest Common Divisor (GCD)
// let a = 48;
// let b = 18;
// let remainder;

// do {
//     remainder = a % b;
//     a = b;
//     b = remainder;
// } while (b !== 0);

// console.log(a);
// // Output: 6

// // Q10. Convert Decimal to Binary
// let n8 = 13;
// let binary2 = "";

// if (n8 === 0) {
//     binary2 = "0";
// } else {
//     do {
//         binary2 = (n8 % 2) + binary2;
//         n8 = Math.floor(n8 / 2);
//     } while (n8 > 0);
// }

// console.log(binary2);
// // Output: 1101