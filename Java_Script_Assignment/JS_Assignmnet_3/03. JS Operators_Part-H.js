// // Type Coercion

// //  Part A - Explicit Type Conversion

// // Q1.
// console.log(Number("25") + 10);
// // Output: 35

// // Q2.
// console.log(String(100) + " rupees");
// // Output: 100 rupees

// // Q3.
// console.log(Boolean(0));
// // Output: false

// // Q4.
// console.log(Boolean("Hello"));
// // Output: true

// // Q5.
// console.log(+"50" * 2);
// // Output: 100


// // Part B - Predict the Output

// // Q6.
// console.log("10" - 5); // Output: 5
// console.log("10" + 5); // Output: 105
// console.log("10" * 2); // Output: 20
// console.log("10" / 2); // Output: 5

// // Q7.
// console.log("5" - "2"); // Output: 3
// console.log("5" + "2"); // Output: 52
// console.log("5" * "2"); // Output: 10
// console.log("5" / "2"); // Output: 2.5

// // Q8.
// console.log(Number("123"));      // Output: 123
// console.log(Number("123abc"));   // Output: NaN
// console.log(Number(true));       // Output: 1
// console.log(Number(false));      // Output: 0
// console.log(Number(null));       // Output: 0
// console.log(Number(undefined));  // Output: NaN

// // Q9.
// console.log(Boolean(0));     // Output: false
// console.log(Boolean(""));    // Output: false
// console.log(Boolean("0"));   // Output: true
// console.log(Boolean([]));    // Output: true
// console.log(Boolean({}));    // Output: true
// console.log(Boolean(null));  // Output: false

// // Q10.
// console.log(String(100));       // Output: 100
// console.log(String(true));      // Output: true
// console.log(String(null));      // Output: null
// console.log(String(undefined)); // Output: undefined
// console.log(100 + "");          // Output: 100


// //  Part C - Advanced Type Coercion

// // Q11.
// console.log("5" + 3 + 2);  // Output: 532
// console.log(5 + 3 + "2");  // Output: 82
// console.log("5" - 3 + 2);  // Output: 4
// console.log(5 - "3" + "2"); // Output: 22

// // Q12.
// console.log(true + true);     // Output: 2
// console.log(true + false);    // Output: 1
// console.log(true + "false");  // Output: truefalse
// console.log(false + "true");  // Output: falsetrue

// // Q13.
// console.log(null + 5);        // Output: 5
// console.log(undefined + 5);   // Output: NaN
// console.log(null + "5");      // Output: null5
// console.log(undefined + "5"); // Output: undefined5

// // Q14.
// console.log([] + []);       // Output: ""
// console.log([] + {});       // Output: [object Object]
// console.log({} + []);       // Output: [object Object]
// console.log({} + {});       // Output: [object Object][object Object]

// // Q15.
// let a1 = "10";
// let b1 = 5;
// let c = a1 + b1;
// let d = a1 - b1;
// let e = +a1 + b1;
// console.log(c, typeof c); // Output: 105 string
// console.log(d, typeof d); // Output: 5 number
// console.log(e, typeof e); // Output: 15 number

// // Q16.
// console.log(!!"Hello");     // Output: true
// console.log(!!"");          // Output: false
// console.log(!!0);           // Output: false
// console.log(!!1);           // Output: true
// console.log(!!null);        // Output: false
// console.log(!!undefined);   // Output: false

// // Q17.
// console.log(Number(""));       // Output: 0
// console.log(Number(" "));      // Output: 0
// console.log(Number("0"));      // Output: 0
// console.log(Number("  25  ")); // Output: 25
// console.log(Number("25px"));   // Output: NaN

// // Q18.
// let val1 = "5";
// let val2 = 2;
// console.log(val1 + val2);      // Output: 52
// console.log(+val1 + val2);     // Output: 7
// console.log(val1 - val2);      // Output: 3
// console.log(val1 * val2);      // Output: 10
// console.log(val1 / val2);      // Output: 2.5


// // Bonus Mixed Practice

// // Q19.
// let count = 5;
// console.log(typeof count++); // Output: number
// console.log(count);          // Output: 6
// console.log(typeof ++count); // Output: number
// console.log(count);          // Output: 7

// // Q20.
// let x1 = "10";
// let y = ++x1;
// console.log(x1, y, typeof x1, typeof y);
// // Output: 11 11 number number

// // Q21.
// let a2 = "5";
// let b2 = a2++;
// console.log(a2, b2, typeof a2, typeof b2);
// // Output: 6 5 number number

// // Q22.
// console.log(typeof (1 + "2")); // Output: string
// console.log(typeof (1 - "2")); // Output: number
// console.log(typeof (1 * "2")); // Output: number
// console.log(typeof (1 / "2")); // Output: number

// // Q23.
// let val = null;
// console.log(typeof val);  // Output: object
// console.log(val + 1);     // Output: 1
// console.log(val - 1);     // Output: -1
// console.log(val * 1);     // Output: 0
// console.log(Boolean(val)); // Output: false