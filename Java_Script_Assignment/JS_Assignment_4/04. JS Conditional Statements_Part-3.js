// // Conditional Statements

// //E: switch Statement

// // Q1.
// let month = 2;

// switch (month) {
//     case 1:
//     case 3:
//     case 5:
//     case 7:
//     case 8:
//     case 10:
//     case 12:
//         console.log("31 days");
//         break;
//     case 4:
//     case 6:
//     case 9:
//     case 11:
//         console.log("30 days");
//         break;
//     case 2:
//         console.log("28 days");
//         break;
//     default:
//         console.log("Invalid Month");
// }
// // Output: 28 days

// // Q2.
// let character = "a";

// switch (character.toLowerCase()) {
//     case "a":
//     case "e":
//     case "i":
//     case "o":
//     case "u":
//         console.log("Vowel");
//         break;
//     default:
//         console.log("Consonant");
// }
// // Output: Vowel

// // Q3.
// let seasonNumber = 3;

// switch (seasonNumber) {
//     case 1:
//     case 2:
//         console.log("Winter");
//         break;
//     case 3:
//     case 4:
//         console.log("Summer");
//         break;
//     default:
//         console.log("Invalid Number");
// }
// // Output: Summer

// // Q4.
// let marks = 78;

// switch (true) {
//     case marks >= 75:
//         console.log("Distinction");
//         break;
//     case marks >= 60:
//         console.log("1st Class");
//         break;
//     case marks >= 50:
//         console.log("2nd Class");
//         break;
//     case marks >= 35:
//         console.log("3rd Class");
//         break;
//     default:
//         console.log("Failed");
// }
// // Output: Distinction

// // Q5.
// let role = "admin";
// let action = "delete";

// switch (role) {
//     case "admin":
//         switch (action) {
//             case "create":
//                 console.log("Create Action");
//                 break;
//             case "edit":
//                 console.log("Edit Action");
//                 break;
//             case "delete":
//                 console.log("Delete Action");
//                 break;
//             default:
//                 console.log("Invalid Action");
//         }
//         break;
//     case "user":
//         console.log("Limited Access");
//         break;
//     default:
//         console.log("Invalid Role");
// }
// // Output: Delete Action

// // Q6.
// let fruit = "mango";

// switch (fruit) {
//     case "apple":
//         console.log("Apple is red");
//     case "mango":
//         console.log("Mango is yellow");
//     case "banana":
//         console.log("Banana is yellow");
//     default:
//         console.log("Unknown fruit");
// }
// // Output:
// // Mango is yellow
// // Banana is yellow
// // Unknown fruit
// // Explanation: Missing break statements cause fall-through.

// // Corrected code:
// switch (fruit) {
//     case "apple":
//         console.log("Apple is red");
//         break;
//     case "mango":
//         console.log("Mango is yellow");
//         break;
//     case "banana":
//         console.log("Banana is yellow");
//         break;
//     default:
//         console.log("Unknown fruit");
// }
// // Output: Mango is yellow

// // Q7.
// let value = "0";

// switch (value) {
//     case 0:
//         console.log("Number zero");
//         break;
//     case "0":
//         console.log("String zero");
//         break;
//     case false:
//         console.log("Boolean false");
//         break;
//     case null:
//         console.log("Null value");
//         break;
//     case undefined:
//         console.log("Undefined value");
//         break;
//     default:
//         console.log("Unknown value");
// }
// // Output: String zero
// // Explanation: switch uses strict comparison, so 0, "0", and false are different.

// // Q8.
// let num1 = 10;
// let num2 = 3;
// let operator = "**";

// switch (operator) {
//     case "+":
//         console.log(num1 + num2);
//         break;
//     case "-":
//         console.log(num1 - num2);
//         break;
//     case "*":
//         console.log(num1 * num2);
//         break;
//     case "/":
//         if (num2 === 0) {
//             console.log("Cannot divide by zero");
//         } else {
//             console.log(num1 / num2);
//         }
//         break;
//     case "%":
//         if (num2 === 0) {
//             console.log("Cannot calculate remainder with zero");
//         } else {
//             console.log(num1 % num2);
//         }
//         break;
//     case "**":
//         console.log(num1 ** num2);
//         break;
//     default:
//         console.log("Invalid Operator");
// }
// // Output: 1000

// // Q9.
// let day = 15;

// switch (true) {
//     case day >= 1 && day <= 10:
//         console.log("Beginning of the month");
//         break;
//     case day >= 11 && day <= 20:
//         console.log("Middle of the month");
//         break;
//     case day >= 21 && day <= 31:
//         console.log("End of the month");
//         break;
//     default:
//         console.log("Invalid Day");
// }
// // Output: Middle of the month

// // Q10.
// let category = "veg";
// let item = "paneer";
// let size = "full";
// let foodPrice = 0;

// switch (category) {
//     case "veg":
//         switch (item) {
//             case "paneer":
//                 switch (size) {
//                     case "half":
//                         foodPrice = 120;
//                         break;
//                     case "full":
//                         foodPrice = 220;
//                         break;
//                     default:
//                         console.log("Invalid Size");
//                 }
//                 break;
//             case "pizza":
//                 switch (size) {
//                     case "half":
//                         foodPrice = 150;
//                         break;
//                     case "full":
//                         foodPrice = 300;
//                         break;
//                     default:
//                         console.log("Invalid Size");
//                 }
//                 break;
//             default:
//                 console.log("Invalid Veg Item");
//         }
//         break;
//     case "nonveg":
//         switch (item) {
//             case "chicken":
//                 switch (size) {
//                     case "half":
//                         foodPrice = 180;
//                         break;
//                     case "full":
//                         foodPrice = 320;
//                         break;
//                     default:
//                         console.log("Invalid Size");
//                 }
//                 break;
//             default:
//                 console.log("Invalid Nonveg Item");
//         }
//         break;
//     default:
//         console.log("Invalid Category");
// }

// if (foodPrice > 0) {
//     console.log("Category:", category);
//     console.log("Item:", item);
//     console.log("Size:", size);
//     console.log("Price: ₹" + foodPrice);
// }
// // Output:
// // Category: veg
// // Item: paneer
// // Size: full
// // Price: ₹220


// // F: Ternary Operator

// // Q1.
// let number1 = 14;
// console.log(number1 % 7 === 0 ? "Divisible by 7" : "Not Divisible by 7");
// // Output: Divisible by 7

// // Q2.
// let temperature = 32;
// console.log(temperature >= 30 ? "Hot Day" : "Pleasant Day");
// // Output: Hot Day

// // Q3.
// let text = "";
// console.log(text === "" ? "Empty String" : "String has content");
// // Output: Empty String

// // Q4.
// let age = 16;
// console.log(age < 13 ? "Child" : age <= 19 ? "Teenager" : "Adult");
// // Output: Teenager

// // Q5.
// let a = 20;
// let b = 35;
// let c = 25;
// console.log(a >= b && a >= c ? a : b >= c ? b : c);
// // Output: 35

// // Q6.
// let studentMarks = 65;
// console.log(
//     studentMarks >= 75 ? "Distinction" :
//     studentMarks >= 60 ? "First Class" :
//     studentMarks >= 50 ? "Second Class" :
//     studentMarks >= 35 ? "Pass" : "Fail"
// );
// // Output: First Class

// // Q7.
// let number2 = -7;
// console.log(
//     number2 === 0 ? "Zero" :
//     number2 > 0 ?
//         (number2 % 2 === 0 ? "Positive Even" : "Positive Odd") :
//         (number2 % 2 === 0 ? "Negative Even" : "Negative Odd")
// );
// // Output: Negative Odd

// // Q8.
// let year = 2024;
// console.log(
//     year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0)
//         ? "Leap Year"
//         : "Not a Leap Year"
// );
// // Output: Leap Year

// // Q9.
// let role1 = "admin";
// let action1 = "edit";

// console.log(
//     role1 === "admin" ?
//         (action1 === "delete" ? "Admin Delete" :
//         action1 === "edit" ? "Admin Edit" : "Admin Other") :
//     role1 === "user" ?
//         (action1 === "view" ? "User View" : "User Restricted") :
//         "Invalid Role"
// );
// // Output: Admin Edit

// // Q10.
// let cartTotal = 6000;

// let orderSummary = cartTotal >= 5000
//     ? { discount: "20%", payable: cartTotal * 0.80 }
//     : cartTotal >= 2000
//         ? { discount: "10%", payable: cartTotal * 0.90 }
//         : cartTotal >= 1000
//             ? { discount: "5%", payable: cartTotal * 0.95 }
//             : { discount: "0%", payable: cartTotal };

// console.log(orderSummary);
// // Output: { discount: '20%', payable: 4800 }