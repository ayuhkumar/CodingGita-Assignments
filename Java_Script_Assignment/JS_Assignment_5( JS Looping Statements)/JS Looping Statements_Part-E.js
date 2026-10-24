// // Q1.
// let num = 1;

// for (let i = 1; i <= 4; i++) {
//     let row = "";
//     for (let j = 1; j <= i; j++) {
//         row += num + " ";
//         num++;
//     }
//     console.log(row);
// }

// // Q2.
// for (let i = 1; i <= 4; i++) {
//     let row = "";
//     for (let j = 1; j <= i; j++) {
//         row += i + " ";
//     }
//     console.log(row);
// }

// // Q3.
// let value = 1;

// for (let i = 1; i <= 4; i++) {
//     let row = "";
//     for (let j = 1; j <= i; j++) {
//         row += value + " ";
//         value++;
//     }
//     console.log(row);
// }

// // Q4.
// for (let i = 1; i <= 4; i++) {
//     let row = "";

//     for (let j = 1; j <= 4; j++) {
//         if (i === 1 || i === 4 || j === 1 || j === 4) {
//             row += "* ";
//         } else {
//             row += "  ";
//         }
//     }

//     console.log(row);
// }

// // Q5.
// for (let i = 1; i <= 6; i++) {
//     let row = "";
//     let symbol = i % 2 === 1 ? "#" : "$";

//     for (let j = 1; j <= i; j++) {
//         row += symbol + " ";
//     }

//     console.log(row);
// }

// // Q6.
// for (let i = 1; i <= 5; i++) {
//     let row = "";

//     for (let j = 0; j < i; j++) {
//         row += String.fromCharCode(65 + j) + " ";
//     }

//     console.log(row);
// }

// // Q7.
// for (let i = 1; i <= 5; i++) {
//     let row = "";

//     for (let j = 1; j <= i; j++) {
//         if (j === 1 || j === i || i === 5) {
//             row += "* ";
//         } else {
//             row += "  ";
//         }
//     }

//     console.log(row);
// }

// // Q8.
// for (let i = 5; i >= 1; i--) {
//     let row = "";

//     for (let j = 1; j <= i; j++) {
//         row += "*";
//     }

//     console.log(row);
// }

// // Q9.
// for (let i = 5; i >= 1; i--) {
//     let row = "";

//     for (let j = 1; j <= i; j++) {
//         row += i + " ";
//     }

//     console.log(row);
// }

// // Q10.
// for (let i = 5; i >= 1; i--) {
//     let row = "";

//     for (let j = 1; j <= i; j++) {
//         row += j + " ";
//     }

//     console.log(row);
// }

// // Q11.
// let number = 15;

// for (let i = 5; i >= 1; i--) {
//     let row = "";

//     for (let j = 1; j <= i; j++) {
//         row += number + " ";
//         number--;
//     }

//     console.log(row);
// }

// // Q12.
// for (let i = 5; i >= 1; i--) {
//     let row = "";

//     for (let j = 1; j <= i; j++) {
//         if (i === 5 || j === 1 || j === i) {
//             row += "* ";
//         } else {
//             row += "  ";
//         }
//     }

//     console.log(row);
// }

// // Q13.
// for (let i = 1; i <= 5; i++) {
//     let row = "";

//     for (let j = 1; j <= 5; j++) {
//         if (i === j) {
//             row += "  ";
//         } else {
//             row += "* ";
//         }
//     }

//     console.log(row);
// }

// // Q14.
// for (let i = 1; i <= 5; i++) {
//     let row = "";

//     for (let j = 1; j <= 10; j++) {
//         let product = i * j;

//         if (product % 2 === 0) {
//             row += product + " ";
//         }
//     }

//     console.log(row);
// }

// // Q15.
// for (let i = 1; i <= 3; i++) {
//     let row = "";

//     for (let j = 1; j <= 3 - i; j++) {
//         row += "  ";
//     }

//     for (let j = 1; j <= i; j++) {
//         row += j + " ";
//     }

//     for (let j = i - 1; j >= 1; j--) {
//         row += j + " ";
//     }

//     console.log(row);
// }