
// // C] COMPARISON OPERATORS

// // 1. LOOSE EQUALITY 


// // 1. 

// console.log("25" == 25);

// // Output:
// // true

// // Explanation:
// // == performs type conversion before comparison.
// // "25" is converted into the number 25.



// // 2. 

// console.log(0 == false);

// // Output:
// // true



// // 3. 

// console.log(10 == "10");
// console.log(null == undefined);

// // Output:
// // true
// // true

// // Explanation:
// // 10 and "10" become equal after type conversion.
// // null and undefined are loosely equal using ==.



// // 4. 

// console.log("" == 0);
// console.log([] == false);

// // Output:
// // true
// // true

// // Explanation:
// // The empty string "" is converted to 0.
// // An empty array [] is converted to an empty string,
// // which is then converted to 0.



// // 5. 

// console.log(NaN == NaN);

// // Output:
// // false

// // Explanation:
// // NaN represents an invalid or unknown numeric result.
// // NaN is not equal to itself.
// // Therefore, NaN == NaN returns false.



// // 2. LOOSE INEQUALITY !=



// // 1. 

// console.log("18" != 18);

// // Output:
// // false

// // Explanation:
// // == type conversion makes "18" and 18 equal.
// // Therefore, != returns false.



// // 2. 

// let storedPassword = "1234";
// let enteredPassword = 1234;

// console.log(storedPassword != enteredPassword);

// // Output:
// // false

// // Explanation:
// // The values become equal after type conversion.



// // 3. 

// console.log(5 != "5");
// console.log(0 != false);

// // Output:
// // false
// // false



// // 4. 

// console.log(null != undefined);
// console.log("" != 0);

// // Output:
// // false
// // false



// // 5. 

// console.log(NaN != NaN);

// // Output:
// // true

// // Explanation:
// // NaN is not equal to itself.
// // Therefore, the inequality comparison returns true.




// // 3. STRICT EQUALITY ===



// // 1. 

// console.log("25" === 25);

// // Output:
// // false

// // Explanation:
// // === compares both value and data type.
// // "25" is a string while 25 is a number.
// // Therefore, they are not strictly equal.



// // 2.

// console.log(0 === false);
// console.log(null === undefined);

// // Output:
// // false
// // false

// // Explanation:
// // 0 is a number and false is a boolean.
// // null and undefined are different data types.



// // 3. 

// console.log(10 === "10");
// console.log(true === 1);

// // Output:
// // false
// // false



// // 4. 

// console.log("" === 0);
// console.log([] === false);

// // Output:
// // false
// // false

// // Explanation:
// // Strict equality does not perform type conversion.
// // The values have different types.



// // 5. 

// // Explanation:
// // === is generally preferred because it checks both value and type.
// // It does not perform unexpected type conversion.
// // This makes the code more predictable and easier to understand.




// // 4. STRICT INEQUALITY !==



// // 1. 

// console.log("18" !== 18);

// // Output:
// // true

// // Explanation:
// // "18" is a string and 18 is a number.
// // Since their types are different, !== returns true.



// // 2. 

// console.log(0 !== false);
// console.log(null !== undefined);

// // Output:
// // true
// // true

// // Explanation:
// // 0 is a number and false is a boolean.
// // null and undefined are different types.



// // 3. 

// console.log(5 !== "5");
// console.log(true !== 1);

// // Output:
// // true
// // true



// // 4. 

// console.log("" !== 0);
// console.log(NaN !== NaN);

// // Output:
// // true
// // true

// // Explanation:
// // "" is a string while 0 is a number.
// // Therefore, they are strictly different.
// //
// // NaN is not equal to itself.
// // Therefore, NaN !== NaN returns true.