
// // B] ASSIGNMENT OPERATORS

// // 1. SIMPLE ASSIGNMENT =



// // 1. 

// let studentName = "Priya";
// let marks = 92;

// console.log(studentName);
// console.log(marks);

// // Output:
// // Priya
// // 92



// // 2. 

// let score = 0;

// console.log(score);

// // Output:
// // 0



// // 3. 

// let a = b = c = 50;

// console.log(a);
// console.log(b);
// console.log(c);

// // Output:
// // 50
// // 50
// // 50



// // 4. 

// let x;
// x = 100;

// console.log(x);

// // Output:
// // 100

// // Explanation:
// // The variable x is declared first and then assigned the value 100.



// // 5. 

// let p = 15;
// let q = p;

// q = 30;

// console.log(p, q);

// // Output:
// // 15 30

// // Explanation:
// // q initially receives a copy of the value of p.
// // Changing q later does not change p.




// // 2. ADD AND ASSIGN +=



// // 1.
// let playerScore = 80;

// playerScore += 25;

// console.log(playerScore);

// // Output:
// // 105



// // 2. 

// let walletBalance = 1500;

// walletBalance += 120;

// console.log(walletBalance);

// // Output:
// // 1620



// // 3. 

// let count = 10;

// count += 5;

// console.log(count);

// // Output:
// // 15



// // 4.

// let msg = "Good";

// msg += " Morning";

// console.log(msg);

// // Output:
// // Good Morning

// // Explanation:
// // += also works with strings and joins the strings together.



// // 5. 
// let n = 20;

// n += "5";

// console.log(n);

// // Output:
// // 205

// // Explanation:
// // Since "5" is a string, += performs string concatenation.
// // 20 + "5" becomes "205".




// // 3. SUBTRACT AND ASSIGN -=



// // 1. 
// let health = 100;

// health -= 35;

// console.log(health);

// // Output:
// // 65



// // 2. 

// let stock = 300;

// stock -= 45;

// console.log(stock);

// // Output:
// // 255



// // 3.

// let lives = 5;

// lives -= 2;

// console.log(lives);

// // Output:
// // 3



// // 4. 

// let num = "40";

// num -= 15;

// console.log(num);

// // Output:
// // 25

// // Explanation:
// // The -= operator converts the numeric string "40" into a number.
// // 40 - 15 = 25.



// // 5. 

// let x2 = "abc";

// x2 -= 5;

// console.log(x2);

// // Output:
// // NaN

// // Explanation:
// // "abc" cannot be converted into a number.
// // Therefore, the subtraction results in NaN.



// // 4. MULTIPLY AND ASSIGN *=



// // 1.
// let price = 500;

// price *= 1.18;

// console.log(price);

// // Output:
// // 590



// // 2.

// let quantity = 8;

// quantity *= 3;

// console.log(quantity);

// // Output:
// // 24



// // 3. 

// let amount = 200;

// amount *= 1.1;

// console.log(amount);

// // Output:
// // 220



// // 4. 

// let val = "7";

// val *= 3;

// console.log(val);

// // Output:
// // 21

// // Explanation:
// // The string "7" is converted into the number 7.
// // 7 * 3 = 21.



// // 5. 

// let y = "hello";

// y *= 2;

// console.log(y);

// // Output:
// // NaN

// // Explanation:
// // "hello" cannot be converted into a number.
// // Therefore, multiplication results in NaN.




// // 5. DIVIDE AND ASSIGN /=



// // 1. 

// let chocolates = 180;

// chocolates /= 6;

// console.log(chocolates);

// // Output:
// // 30



// // 2. 

// let distance = 300;

// distance /= 5;

// console.log(distance);

// // Output:
// // 60



// // 3. 

// let total = 400;

// total /= 8;

// console.log(total);

// // Output:
// // 50



// // 4.

// let num2 = "100";

// num2 /= 4;

// console.log(num2);

// // Output:
// // 25

// // Explanation:
// // The string "100" is converted into the number 100.
// // 100 / 4 = 25.



// // 5. 

// let z = 50;

// z /= 0;

// console.log(z);

// // Output:
// // Infinity

// // Explanation:
// // Dividing a positive number by zero results in Infinity in JavaScript.




// // 6. MODULUS AND ASSIGN %=



// // 1. 

// let number = 47;

// number %= 6;

// console.log(number);

// // Output:
// // 5



// // 2. 

// let counter = 23;

// counter %= 12;

// console.log(counter);

// // Output:
// // 11



// // 3. 

// let num3 = 29;

// num3 %= 5;

// console.log(num3);

// // Output:
// // 4



// // 4. 

// let x3 = "17";

// x3 %= 3;

// console.log(x3);

// // Output:
// // 2

// // Explanation:
// // "17" is converted into the number 17.
// // 17 % 3 = 2.



// // 5. 

// let m = 15;

// m %= 0;

// console.log(m);

// // Output:
// // NaN

// // Explanation:
// // A remainder cannot be calculated when the divisor is zero.
// // Therefore, the result is NaN.



// // 7. EXPONENTIATION AND ASSIGN **=



// // 1. 

// let cubeSide = 5;

// cubeSide **= 3;

// console.log(cubeSide);

// // Output:
// // 125



// // 2.

// let squareNumber = 4;

// squareNumber **= 2;

// console.log(squareNumber);

// // Output:
// // 16



// // 3. 

// let base = 2;

// base **= 5;

// console.log(base);

// // Output:
// // 32



// // 4. 

// let n2 = 4;

// n2 **= 0.5;

// console.log(n2);

// // Output:
// // 2

// // Explanation:
// // 4 ** 0.5 means the square root of 4.
// // Therefore, the result is 2.



// // 5. 

// let p2 = 2;

// p2 **= -1;

// console.log(p2);

// // Output:
// // 0.5

// // Explanation:
// // 2 ** -1 = 1 / 2 = 0.5


