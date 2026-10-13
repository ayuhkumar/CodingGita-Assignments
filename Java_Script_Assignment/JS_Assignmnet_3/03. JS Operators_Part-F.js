//  Logical Operators

//Logical AND (&&)

// Q1.
let username = "admin";
let password = 1234;
console.log(username === "admin" && password === 1234);
// Output: true

// Q2.
let isLoggedIn = true;
let hasPermission = true;
console.log(isLoggedIn && hasPermission);
// Output: true

// Q3.
let inStock = true;
let price = 800;
console.log(inStock && price < 1000);
// Output: true

// Q4.
let marks = 75;
let attendance = 80;
console.log(marks > 65 && attendance > 70);
// Output: true

// Q5.
let isWeekend = true;
let isHoliday = false;
console.log(isWeekend && isHoliday);
// Output: false

// Q6.
let a = 0;
let b = 10;
let result = a && b;
console.log(result);
// Output: 0
// Explanation: && returns the first falsy value.

// Q7.
let x = 5;
let y = 10;
let result1 = (x > 3 && y) || 0;
console.log(result1);
// Output: 10
// Explanation: Both conditions are truthy, so the result is 10.

// Q8.
let p = "Hello";
let q = "";
let r = "World";
let result2 = p && q && r;
console.log(result2);
// Output: ""
// Explanation: && returns the first falsy value, which is "".

// Q9.
let val = 5;
let condition = val && (val = 0);
console.log(condition);
console.log(val);
// Output: 0
// Output: 0
// Explanation: Since val is truthy, val = 0 executes.

// Q10.
let x1 = 10;
let y1 = 20;
let result3 = (x1 && y1) && (x1 > y1);
console.log(result3);
// Output: false


//Logical OR (||)

// Q1.
let passwordCorrect = true;
let otpValid = false;
console.log(passwordCorrect || otpValid);
// Output: true

// Q2.
let isMember = false;
let hasCoupon = true;
console.log(isMember || hasCoupon);
// Output: true

// Q3.
let age = 16;
let height = 155;
console.log(age > 18 || height > 150);
// Output: true

// Q4.
let emailGiven = true;
let phoneGiven = false;
console.log(emailGiven || phoneGiven);
// Output: true

// Q5.
let score = 900;
let timeBonus = true;
console.log(score > 1000 || timeBonus);
// Output: true

// Q6.
let a1 = 0;
let b1 = false;
let c = "";
let d = null;
let e = 42;
let result4 = a1 || b1 || c || d || e;
console.log(result4);
// Output: 42
// Explanation: || returns the first truthy value.

// Q7.
let x2 = "Hello" || 0;
let y2 = 0 || "Hi";
console.log(x2, y2);
// Output: Hello Hi

// Q8.
let a2 = 10;
let b2 = 20;
let result5 = (a2 < 5) || (b2 > 15);
console.log(result5);
// Output: true

// Q9.
let val1 = 5;
let condition1 = val1 || (val1 = 0);
console.log(condition1);
console.log(val1);
// Output: 5
// Output: 5
// Explanation: Since val1 is truthy, val1 = 0 does not execute.

// Q10.
let x3 = "" || 0 || false || null || undefined || "OK";
console.log(x3);
// Output: OK


//Logical NOT (!)

// Q1.
let isBanned = false;
console.log(!isBanned);
// Output: true

// Q2.
let isCompleted = false;
console.log(!isCompleted);
// Output: true

// Q3.
let isOn = true;
console.log(!isOn);
// Output: false

// Q4.
let isActive = false;
console.log(!isActive);
// Output: true

// Q5.
let isReadOnly = false;
console.log(!isReadOnly);
// Output: true

// Q6.
let a3 = 0;
let b3 = 1;
console.log(!a3, !b3);
// Output: true false

// Q7.
let x4 = "Hello";
let y4 = "";
console.log(!x4, !y4);
// Output: false true

// Q8.
let val2 = 5;
let result6 = !val2;
console.log(result6);
// Output: false

// Q9.
let a4 = 10;
let b4 = 20;
let result7 = !(a4 && b4);
console.log(result7);
// Output: false

// Q10.
let x5 = 0;
let y5 = 1;
let result8 = !(x5 || y5);
console.log(result8);
// Output: false