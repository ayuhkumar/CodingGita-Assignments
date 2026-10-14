// Conditional Statements

// if Statement

// Q1.
let num1 = 25;
if (num1 % 5 === 0) {
    console.log("Divisible by 5");
}
// Output: Divisible by 5

// Q2.
let age1 = 65;
if (age1 >= 60) {
    console.log("Senior Citizen");
}
// Output: Senior Citizen

// Q3.
let num2 = 150;
if (num2 > 100) {
    console.log("Big Number");
}
// Output: Big Number

// Q4.
let temperature = 5;
if (temperature < 10) {
    console.log("Very Cold");
}
// Output: Very Cold

// Q5.
let marks1 = 100;
if (marks1 === 100) {
    console.log("Perfect Score");
}
// Output: Perfect Score

// Q6.
let num3 = -10;
if (num3 < 0) {
    console.log("Negative Number");
}
// Output: Negative Number

// Q7.
let userInput = "";
if (userInput === "") {
    console.log("No input provided");
}
// Output: No input provided

// Q8.
let year1 = 1900;
if (year1 % 100 === 0) {
    console.log("Century Year");
}
// Output: Century Year

// Q9.
let num4 = 8;
if (num4 > 0 && num4 % 2 === 0) {
    console.log("Positive Even Number");
}
// Output: Positive Even Number

// Q10.
let marks2 = 75;
if (marks2 >= 35 && marks2 <= 100) {
    console.log("Valid Marks");
}
// Output: Valid Marks


// if...else Statement

// Q1.
let num5 = 7;
if (num5 % 2 === 0) {
    console.log("Even");
} else {
    console.log("Odd");
}
// Output: Odd

// Q2.
let age2 = 20;
if (age2 >= 18) {
    console.log("Eligible");
} else {
    console.log("Not Eligible");
}
// Output: Eligible

// Q3.
let num6 = -5;
if (num6 >= 0) {
    console.log("Positive");
} else {
    console.log("Negative");
}
// Output: Negative

// Q4.
let marks3 = 40;
if (marks3 >= 35) {
    console.log("Passed");
} else {
    console.log("Failed");
}
// Output: Passed

// Q5.
let character = "A";
if (character >= "A" && character <= "Z") {
    console.log("Uppercase Letter");
} else {
    console.log("Not an Uppercase Letter");
}
// Output: Uppercase Letter

// Q6.
let num7 = 12;
if (num7 % 3 === 0) {
    console.log("Divisible by 3");
} else {
    console.log("Not Divisible by 3");
}
// Output: Divisible by 3

// Q7.
let password = "admin123";
if (password === "admin123") {
    console.log("Login Successful");
} else {
    console.log("Incorrect Password");
}
// Output: Login Successful

// Q8.
let year2 = 2024;
if (year2 % 4 === 0) {
    console.log("Leap Year");
} else {
    console.log("Not a Leap Year");
}
// Output: Leap Year

// Q9.
let a = 25;
let b = 40;
if (a > b) {
    console.log("Greater number:", a);
} else {
    console.log("Greater number:", b);
}
// Output: Greater number: 40

// Q10.
let num8 = 0;
if (num8 > 0) {
    console.log("Positive");
} else {
    if (num8 < 0) {
        console.log("Negative");
    } else {
        console.log("Zero");
    }
}
// Output: Zero