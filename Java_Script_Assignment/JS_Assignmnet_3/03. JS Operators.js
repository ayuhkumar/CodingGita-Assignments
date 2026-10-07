
// // ASSIGNMENT : JS OPERATORS

// // A] ARITHMETIC OPERATORS

// // 1. ADDITION +



// // 1. 

// console.log(15 + 27);

// // Output:
// // 42



// // 2. 

// let bookPrice = 350;
// let penPrice = 45;

// console.log(bookPrice + penPrice);

// // Output:
// // 395



// // 3. 

// console.log("25" + 10);

// // Output:
// // 2510

// // Explanation:
// // The + operator performs string concatenation when one of the values is a string.
// // Therefore, number 10 is converted to a string and joined with "25".



// // 4. 

// let wallet = 2000;
// let item1 = 750;
// let item2 = 320;

// let totalSpent = item1 + item2;
// let remainingBalance = wallet - totalSpent;

// console.log(totalSpent);
// console.log(remainingBalance);

// // Output:
// // 1070
// // 930



// // 5. 
// console.log(5 + "5" + 5);
// console.log(5 + 5 + "5");
// console.log("5" + 5 + 5);

// // Output:
// // 555
// // 105
// // 555

// // Explanation:
// // 5 + "5" becomes "55", then "55" + 5 becomes "555".
// // 5 + 5 is calculated first because both are numbers.
// // 10 + "5" becomes "105".
// // "5" + 5 becomes "55", then "55" + 5 becomes "555".



// // 6.

// console.log(15 + 27);

// // Output:
// // 42


// // 7.

// let bookPrice = 350;
// let penPrice = 45;

// console.log(bookPrice + penPrice);

// // Output:
// // 395


// // 8.

// console.log("25" + 10);

// // Output:
// // 2510

// // Explanation:
// // "25" is a string, so the + operator performs string concatenation.
// // The number 10 is converted into a string.
// // Therefore, "25" + 10 gives "2510".


// // 9.

// let wallet = 2000;
// let item1 = 750;
// let item2 = 320;

// let totalSpent = item1 + item2;
// let remainingBalance = wallet - totalSpent;

// console.log(totalSpent);
// console.log(remainingBalance);

// // Output:
// // 1070
// // 930

// // Explanation:
// // Total spent = 750 + 320 = 1070
// // Remaining balance = 2000 - 1070 = 930


// // 10. 

// console.log(5 + "5" + 5);
// console.log(5 + 5 + "5");
// console.log("5" + 5 + 5);

// // Output:
// // 555
// // 105
// // 555

// // Explanation:
// // 5 + "5" becomes "55", then "55" + 5 becomes "555".
// //
// // 5 + 5 is calculated first because both are numbers.
// // 10 + "5" becomes "105".
// //
// // "5" + 5 becomes "55", then "55" + 5 becomes "555".




// // 2. SUBTRACTION -


// // 1. 

// console.log(100 - 37);

// // Output:
// // 63



// // 2.


// let water = 500;
// let usedWater = 175;

// console.log(water - usedWater);

// // Output:
// // 325



// // 3. 

// console.log("50" - 20);
// console.log("50" - "20");

// // Output:
// // 30
// // 30

// // Explanation:
// // The - operator converts numeric strings into numbers before subtraction.
// // Therefore, both expressions produce 30.


// // 4.

// let apples = 240;
// let morningSale = 95;
// let eveningSale = 67;

// let applesLeft = apples - morningSale - eveningSale;

// console.log(applesLeft);

// // Output:
// // 78



// // 5. 

// console.log("100" - 50);
// console.log("abc" - 10);
// console.log(10 - "5" - "2");
// console.log("10" - "5" - "2");

// // Output:
// // 50
// // NaN
// // 3
// // 3

// // Explanation:
// // "100" is converted to the number 100.
// // "abc" cannot be converted into a number, so the result is NaN.
// // 10 - 5 = 5, then 5 - 2 = 3.
// // "10" and "5" are converted to numbers, so the result is also 3.

// // 6. What is the output of 100 - 37?

// console.log(100 - 37);

// // Output:
// // 63


// // 7.

// let totalWater = 500;
// let usedWater = 175;

// console.log(totalWater - usedWater);

// // Output:
// // 325


// // 8.

// console.log("50" - 20);
// console.log("50" - "20");

// // Output:
// // 30
// // 30

// // Explanation:
// // The - operator converts numeric strings into numbers.
// // Therefore, both expressions give the same result: 30.


// // 9. 

// let totalApples = 240;
// let morningSale = 95;
// let eveningSale = 67;

// let applesLeft = totalApples - morningSale - eveningSale;

// console.log(applesLeft);

// // Output:
// // 78

// // Explanation:
// // 240 - 95 - 67 = 78


// // 10.

// console.log("100" - 50);
// console.log("abc" - 10);
// console.log(10 - "5" - "2");
// console.log("10" - "5" - "2");

// // Output:
// // 50
// // NaN
// // 3
// // 3

// // Explanation:
// // "100" is converted into the number 100.
// // 100 - 50 = 50.
// //
// // "abc" cannot be converted into a number.
// // Therefore, the result is NaN.
// //
// // 10 - "5" gives 5.
// // 5 - "2" gives 3.
// //
// // "10" - "5" gives 5.
// // 5 - "2" gives 3.





// // 3. MULTIPLICATION *


// // 1. 

// console.log(12 * 8);

// // Output:
// // 96



// // 2. 


// let pizzaPrice = 299;
// let pizzaQuantity = 4;

// console.log(pizzaPrice * pizzaQuantity);

// // Output:
// // 1196



// // 3. 

// console.log("7" * 6);
// console.log("7" * "6");

// // Output:
// // 42
// // 42

// // Explanation:
// // The * operator converts numeric strings into numbers.



// // 4. 


// let unitsPerHour = 45;
// let hours = 8;

// console.log(unitsPerHour * hours);

// // Output:
// // 360



// // 5. 

// console.log("5" * 3 * "2");
// console.log("abc" * 4);
// console.log(10 * "2.5");
// console.log("10" * "2.5" * "0");

// // Output:
// // 30
// // NaN
// // 25
// // 0

// // Explanation:
// // "5" is converted to 5 and "2" is converted to 2.
// // "abc" cannot be converted to a number, so the result is NaN.
// // "2.5" is converted to 2.5.
// // Multiplying by "0" results in 0.


// // 6. 

// console.log(12 * 8);

// // Output:
// // 96


// // 7. 

// let pizzaPrice = 299;
// let pizzaQuantity = 4;

// console.log(pizzaPrice * pizzaQuantity);

// // Output:
// // 1196


// // 8.

// console.log("7" * 6);
// console.log("7" * "6");

// // Output:
// // 42
// // 42

// // Explanation:
// // The * operator converts numeric strings into numbers.
// // Therefore, both expressions give 42.


// // 9. 

// let unitsPerHour = 45;
// let hours = 8;

// console.log(unitsPerHour * hours);

// // Output:
// // 360

// // Expression:
// // 45 * 8 = 360


// // 10.

// console.log("5" * 3 * "2");
// console.log("abc" * 4);
// console.log(10 * "2.5");
// console.log("10" * "2.5" * "0");

// // Output:
// // 30
// // NaN
// // 25
// // 0

// // Explanation:
// // "5" is converted to 5 and "2" is converted to 2.
// // Therefore, 5 * 3 * 2 = 30.
// //
// // "abc" cannot be converted into a number.
// // Therefore, "abc" * 4 gives NaN.
// //
// // "2.5" is converted into the number 2.5.
// // Therefore, 10 * 2.5 = 25.
// //
// // "10", "2.5", and "0" are converted into numbers.
// // Therefore, 10 * 2.5 * 0 = 0.









// // 4. DIVISION /



// // 1. 

// console.log(144 / 12);

// // Output:
// // 12



// // 2. 


// let students = 360;
// let classrooms = 9;

// console.log(students / classrooms);

// // Output:
// // 40



// // 3. 

// console.log("100" / 4);
// console.log("100" / "4");

// // Output:
// // 25
// // 25

// // Explanation:
// // The / operator converts numeric strings into numbers.



// // 4.


// let bill = 2400;
// let friends = 6;

// console.log(bill / friends);

// // Output:
// // 400



// // 5. 

// console.log(10 / 0);
// console.log(-10 / 0);
// console.log(0 / 0);
// console.log("20" / "4" / 2);
// console.log("abc" / 5);

// // Output:
// // Infinity
// // -Infinity
// // NaN
// // 2.5
// // NaN

// // Explanation:
// // A positive number divided by zero gives Infinity.
// // A negative number divided by zero gives -Infinity.
// // Zero divided by zero gives NaN.
// // "20" / "4" becomes 20 / 4 = 5, then 5 / 2 = 2.5.
// // "abc" cannot be converted to a number, so the result is NaN.


// // 6. What is the output of 144 / 12?

// console.log(144 / 12);

// // Output:
// // 12


// // 7. 

// let students = 360;
// let classrooms = 9;

// console.log(students / classrooms);

// // Output:
// // 40


// // 8.

// console.log("100" / 4);
// console.log("100" / "4");

// // Output:
// // 25
// // 25

// // Explanation:
// // The / operator converts numeric strings into numbers.
// // Therefore, both expressions give 25.


// // 9.

// let totalBill = 2400;
// let friends = 6;

// console.log(totalBill / friends);

// // Output:
// // 400

// // Expression:
// // 2400 / 6 = 400


// // 10. 

// console.log(10 / 0);
// console.log(-10 / 0);
// console.log(0 / 0);
// console.log("20" / "4" / 2);
// console.log("abc" / 5);

// // Output:
// // Infinity
// // -Infinity
// // NaN
// // 2.5
// // NaN

// // Explanation:
// // 10 / 0 gives Infinity because a positive number is divided by zero.
// //
// // -10 / 0 gives -Infinity because a negative number is divided by zero.
// //
// // 0 / 0 gives NaN because zero divided by zero is undefined.
// //
// // "20" / "4" converts both strings into numbers.
// // 20 / 4 = 5, and 5 / 2 = 2.5.
// //
// // "abc" cannot be converted into a number.
// // Therefore, "abc" / 5 gives NaN.









// // 5. MODULUS %



// // 1. 

// console.log(29 % 5);

// // Output:
// // 4



// // 2. 

// let chocolates = 23;
// let boxSize = 4;

// console.log(chocolates % boxSize);

// // Output:
// // 3



// // 3. 

// console.log(0 % 7);
// console.log(15 % 0);

// // Output:
// // 0
// // NaN

// // Explanation:
// // 0 divided by 7 has a remainder of 0.
// // Division by zero is not defined, so 15 % 0 gives NaN.



// // 4. 


// let pages = 47;
// let pagesPerSheet = 6;

// let fullSheets = Math.floor(pages / pagesPerSheet);
// let remainingPages = pages % pagesPerSheet;

// console.log(fullSheets);
// console.log(remainingPages);

// // Output:
// // 7
// // 5



// // 5. 

// console.log(17 % 5);
// console.log(-17 % 5);
// console.log(17 % -5);
// console.log(-17 % -5);
// console.log(10 % 0);

// // Output:
// // 2
// // -2
// // 2
// // -2
// // NaN

// // Explanation:
// // JavaScript's remainder operator keeps the sign of the dividend,
// // which is the number on the left side.
// // Therefore:
// // 17 % 5 = 2
// // -17 % 5 = -2
// // 17 % -5 = 2
// // -17 % -5 = -2
// // Any remainder operation with zero as the divisor gives NaN.

// // 6. 

// console.log(29 % 5);

// // Output:
// // 4


// // 7. 

// let chocolates = 23;
// let boxSize = 4;

// console.log(chocolates % boxSize);

// // Output:
// // 3


// // 8.

// console.log(0 % 7);
// console.log(15 % 0);

// // Output:
// // 0
// // NaN

// // Explanation:
// // 0 % 7 gives 0 because 0 divided by 7 has a remainder of 0.
// // 15 % 0 gives NaN because division by zero is not defined.


// // 9. 

// let pages = 47;
// let pagesPerSheet = 6;

// let fullSheets = Math.floor(pages / pagesPerSheet);
// let remainingPages = pages % pagesPerSheet;

// console.log(fullSheets);
// console.log(remainingPages);

// // Output:
// // 7
// // 5

// // Explanation:
// // 47 / 6 = 7.8333...
// // There are 7 complete sheets.
// // 47 % 6 = 5 pages left over.


// // 10. 

// console.log(17 % 5);
// console.log(-17 % 5);
// console.log(17 % -5);
// console.log(-17 % -5);
// console.log(10 % 0);

// // Output:
// // 2
// // -2
// // 2
// // -2
// // NaN

// // Explanation:
// // 17 % 5 gives 2.
// //
// // -17 % 5 gives -2 because JavaScript keeps the sign
// // of the dividend, which is the value on the left.
// //
// // 17 % -5 gives 2 because the dividend is positive.
// //
// // -17 % -5 gives -2 because the dividend is negative.
// //
// // 10 % 0 gives NaN because the divisor is zero.



// // 6. EXPONENTIATION **


// // 1.
// console.log(3 ** 4);

// // Output:
// // 81



// // 2.

// let side = 9;
// let area = side ** 2;

// console.log(area);

// // Output:
// // 81



// // 3. 


// console.log(2 ** 5);
// console.log(5 ** 2);

// // Output:
// // 32
// // 25

// // Explanation:
// // 2 ** 5 means 2 × 2 × 2 × 2 × 2 = 32.
// // 5 ** 2 means 5 × 5 = 25.
// // Therefore, they are not the same.



// // 4. 

// console.log(2 ** 3 ** 2);

// console.log((2 ** 3) ** 2);

// console.log(2 ** -3);

// // console.log(-2 ** 2);
// // This causes a SyntaxError because JavaScript does not allow
// // a unary minus directly before exponentiation.
// // Parentheses must be used.

// console.log((-2) ** 2);

// console.log(4 ** 0.5);

// // Output:
// // 512
// // 64
// // 0.125
// // 4
// // 2

// // Explanation:
// // 2 ** 3 ** 2 means 2 ** (3 ** 2) = 2 ** 9 = 512.
// // (2 ** 3) ** 2 means 8 ** 2 = 64.
// // 2 ** -3 means 1 / 2 ** 3 = 0.125.
// // (-2) ** 2 means (-2) × (-2) = 4.
// // 4 ** 0.5 means the square root of 4, which is 2.

// // 6. 

// console.log(3 ** 4);

// // Output:
// // 81


// // 7.

// let side = 9;
// let area = side ** 2;

// console.log(area);

// // Output:
// // 81

// // Explanation:
// // Area = side ** 2
// // Area = 9 ** 2
// // Area = 81


// // 8. 

// console.log(2 ** 5);
// console.log(5 ** 2);

// // Output:
// // 32
// // 25

// // Explanation:
// // 2 ** 5 = 32
// // 5 ** 2 = 25
// // They are not the same.


// // 9. 

// console.log(2 ** 3 ** 2);
// console.log((2 ** 3) ** 2);
// console.log(2 ** -3);

// // console.log(-2 ** 2);
// // This line causes a SyntaxError.
// // JavaScript does not allow unary minus directly before **.
// // Parentheses must be used.

// console.log((-2) ** 2);
// console.log(4 ** 0.5);

// // Output:
// // 512
// // 64
// // 0.125
// // 4
// // 2

// // Explanation:
// // 2 ** 3 ** 2 is right-associative.
// // It is evaluated as 2 ** (3 ** 2).
// // 3 ** 2 = 9.
// // 2 ** 9 = 512.
// //
// // (2 ** 3) ** 2:
// // 2 ** 3 = 8.
// // 8 ** 2 = 64.
// //
// // 2 ** -3:
// // 1 / (2 ** 3) = 1 / 8 = 0.125.
// //
// // (-2) ** 2:
// // (-2) * (-2) = 4.
// //
// // 4 ** 0.5 means the square root of 4.
// // Therefore, the result is 2.


// // 10. 

// let a = 10;
// let b = 0;
// let result = a ** b;

// console.log(result);

// // Output:
// // 1

// // Explanation:
// // Any non-zero number raised to the power 0 is 1.
// // Therefore, 10 ** 0 = 1.