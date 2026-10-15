

// //  C: if...else if...else Statement

// // Q1.
// let month = 4;

// if (month === 12 || month === 1 || month === 2) {
//     console.log("Winter");
// } else if (month >= 3 && month <= 5) {
//     console.log("Summer");
// } else if (month >= 6 && month <= 8) {
//     console.log("Monsoon");
// } else if (month >= 9 && month <= 11) {
//     console.log("Autumn");
// } else {
//     console.log("Invalid Month");
// }
// // Output: Summer

// // Q2.
// let income = 600000;
// let tax;

// if (income < 300000) {
//     tax = 0;
// } else if (income <= 700000) {
//     tax = income * 0.05;
// } else if (income <= 1000000) {
//     tax = income * 0.10;
// } else {
//     tax = income * 0.15;
// }

// console.log("Tax Amount:", tax);
// // Output: Tax Amount: 30000

// // Q3.
// let score = 85;

// if (score >= 90) {
//     console.log("Outstanding");
// } else if (score >= 70) {
//     console.log("Good");
// } else if (score >= 40) {
//     console.log("Average");
// } else {
//     console.log("Needs Improvement");
// }
// // Output: Good

// // Q4.
// let speed = 60;

// if (speed < 40) {
//     console.log("Slow");
// } else if (speed <= 80) {
//     console.log("Normal");
// } else {
//     console.log("Fast");
// }
// // Output: Normal

// // Q5.
// let height = 175;

// if (height < 150) {
//     console.log("Short");
// } else if (height <= 170) {
//     console.log("Average");
// } else {
//     console.log("Tall");
// }
// // Output: Tall

// // Q6.
// let day = 6;

// if (day >= 1 && day <= 5) {
//     console.log("Weekday");
// } else if (day === 6 || day === 7) {
//     console.log("Weekend");
// } else {
//     console.log("Invalid Day");
// }
// // Output: Weekend

// // Q7.
// let units = 120;
// let bill;

// if (units >= 0 && units <= 50) {
//     bill = units * 2;
// } else if (units <= 150 && units > 50) {
//     bill = units * 4;
// } else if (units > 150) {
//     bill = units * 6;
// } else {
//     bill = 0;
//     console.log("Invalid Units");
// }

// if (units >= 0) {
//     console.log("Electricity Bill: ₹" + bill);
// }
// // Output: Electricity Bill: ₹480

// // Q8.
// let attendance = 82;

// if (attendance >= 90) {
//     console.log("Excellent");
// } else if (attendance >= 75) {
//     console.log("Good");
// } else if (attendance >= 50) {
//     console.log("Satisfactory");
// } else {
//     console.log("Poor");
// }
// // Output: Good

// // Q9.
// let marksA = 78;
// let marksB = 92;
// let marksC = 85;

// if (marksA >= marksB && marksA >= marksC) {
//     console.log("Highest Mark:", marksA);
// } else if (marksB >= marksA && marksB >= marksC) {
//     console.log("Highest Mark:", marksB);
// } else {
//     console.log("Highest Mark:", marksC);
// }
// // Output: Highest Mark: 92

// // Q10.
// let number = -7;

// if (number > 0) {
//     if (number % 2 === 0) {
//         console.log("Positive Even");
//     } else {
//         console.log("Positive Odd");
//     }
// } else if (number < 0) {
//     if (number % 2 === 0) {
//         console.log("Negative Even");
//     } else {
//         console.log("Negative Odd");
//     }
// } else {
//     console.log("Zero");
// }
// // Output: Negative Odd


// //D: Nested if Statement

// // Q1.
// let num1 = 15;

// if (num1 > 10) {
//     if (num1 % 3 === 0) {
//         console.log("Greater than 10 and divisible by 3");
//     } else {
//         console.log("Greater than 10 but not divisible by 3");
//     }
// } else {
//     console.log("Number is not greater than 10");
// }
// // Output: Greater than 10 and divisible by 3

// // Q2.
// let age = 20;
// let hasVoterID = true;

// if (age >= 18) {
//     if (hasVoterID) {
//         console.log("Can Vote");
//     } else {
//         console.log("Voter ID Required");
//     }
// } else {
//     console.log("Age is below 18");
// }
// // Output: Can Vote

// // Q3.
// let marks = 85;

// if (marks >= 40) {
//     console.log("Passed");

//     if (marks >= 80) {
//         console.log("Passed with Distinction");
//     }
// } else {
//     console.log("Failed");
// }
// // Output: Passed
// // Output: Passed with Distinction

// // Q4.
// let pin = 1234;
// let correctPin = 1234;
// let balance = 5000;
// let withdrawal = 2000;

// if (pin === correctPin) {
//     if (balance >= withdrawal) {
//         balance = balance - withdrawal;
//         console.log("Withdrawal Successful");
//         console.log("Remaining Balance:", balance);
//     } else {
//         console.log("Insufficient Balance");
//     }
// } else {
//     console.log("Incorrect PIN");
// }
// // Output: Withdrawal Successful
// // Output: Remaining Balance: 3000

// // Q5.
// let year = 2024;

// if (year % 4 === 0) {
//     if (year % 100 === 0) {
//         if (year % 400 === 0) {
//             console.log("Leap Year");
//         } else {
//             console.log("Not a Leap Year");
//         }
//     } else {
//         console.log("Leap Year");
//     }
// } else {
//     console.log("Not a Leap Year");
// }
// // Output: Leap Year

// // Q6.
// let email = "rahul123@gmail.com";

// if (email.includes("@")) {
//     if (email.endsWith(".com")) {
//         if (email.length > 10) {
//             console.log("Valid Email");
//         } else {
//             console.log("Email is too short");
//         }
//     } else {
//         console.log("Email must end with .com");
//     }
// } else {
//     console.log("Email must contain @");
// }
// // Output: Valid Email

// // Q7.
// let cartTotal = 2000;
// let isPremium = true;
// let discount;
// let finalAmount;

// if (cartTotal >= 1000) {
//     if (isPremium) {
//         discount = cartTotal * 0.20;
//     } else {
//         discount = cartTotal * 0.10;
//     }

//     finalAmount = cartTotal - discount;
// } else {
//     finalAmount = cartTotal;
// }

// console.log("Final Amount: ₹" + finalAmount);
// // Output: Final Amount: ₹1600

// // Q8.
// let num2 = 16;

// if (num2 > 0) {
//     if (num2 % 2 === 0) {
//         if (num2 % 4 === 0) {
//             console.log("Positive Even and Divisible by 4");
//         } else {
//             console.log("Positive Even but not Divisible by 4");
//         }
//     } else {
//         console.log("Positive Odd");
//     }
// } else {
//     console.log("Number is not Positive");
// }
// // Output: Positive Even and Divisible by 4

// // Q9.
// let candidateAge = 25;
// let hasDegree = true;
// let experience = 3;

// if (candidateAge >= 21 && candidateAge <= 30) {
//     if (hasDegree) {
//         if (experience >= 2) {
//             console.log("Eligible for Interview");
//         } else {
//             console.log("Insufficient Experience");
//         }
//     } else {
//         console.log("Graduation Degree Required");
//     }
// } else {
//     console.log("Age Criteria Not Met");
// }
// // Output: Eligible for Interview

// // Q10.
// let isPresent = true;
// let internalMarks = 35;
// let externalMarks = 40;

// if (isPresent) {
//     if (internalMarks >= 30) {
//         if (externalMarks >= 35) {
//             console.log("Eligible for Final Exam");
//         } else {
//             console.log("External Marks Insufficient");
//         }
//     } else {
//         console.log("Internal Marks Insufficient");
//     }
// } else {
//     console.log("Student is Absent");
// }
// // Output: Eligible for Final Exam