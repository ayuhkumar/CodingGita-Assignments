// // Part e — Basic Identification (4 Questions)


// // 1. Classify the Types

// let wholeNumber = 25;
// let decimalNumber = 12.5;
// let text = "Hello World";
// let isStudent = true;

// console.log(wholeNumber, typeof wholeNumber);
// console.log(decimalNumber, typeof decimalNumber);
// console.log(text, typeof text);
// console.log(isStudent, typeof isStudent);

// // Output:
// // 25 number
// // 12.5 number
// // Hello World string
// // true boolean


// // 2. Undefined vs Null


// let a;
// let b = null;

// console.log(a, typeof a);
// console.log(b, typeof b);

// // Output:
// // undefined undefined
// // null object

// // Explanation:
// // undefined means a variable has been declared but has not been assigned a value.
// // null means an empty or intentionally missing value has been assigned.
// // typeof null returns "object" because of a historical JavaScript behavior.


// // 3. Number Special Values


// let positiveInfinity = Infinity;
// let negativeInfinity = -Infinity;
// let notANumber = NaN;
// let scientificNumber = 2.5e3;
// let largeNumber = 1_000_000;

// console.log(positiveInfinity, typeof positiveInfinity);
// console.log(negativeInfinity, typeof negativeInfinity);
// console.log(notANumber, typeof notANumber);
// console.log(scientificNumber, typeof scientificNumber);
// console.log(largeNumber, typeof largeNumber);

// // Output:
// // Infinity number
// // -Infinity number
// // NaN number
// // 2500 number
// // 1000000 number



// // 4. String Styles


// let name = "Ayush";

// let singleQuote = 'Hello World';
// let doubleQuote = "Hello JavaScript";
// let templateString = `Hello ${name}`;

// console.log(singleQuote);
// console.log(doubleQuote);
// console.log(templateString);

// // Output:
// // Hello World
// // Hello JavaScript
// // Hello Ayush





// // Part f — Advanced Primitive Types (3 Questions)

// // 5. Symbol Uniqueness


// let symbol1 = Symbol("id");
// let symbol2 = Symbol("id");

// console.log(symbol1 === symbol2);

// let user = {};

// user[symbol1] = "First Value";
// user[symbol2] = "Second Value";

// console.log(user[symbol1]);
// console.log(user[symbol2]);

// // Output:
// // false
// // First Value
// // Second Value

// // Explanation:
// // Every Symbol creates a unique value.
// // Even if two Symbols have the same description,
// // they are not equal to each other.


// // 6. BigInt Precision


// let normalNumber = 9007199254740991;

// console.log(normalNumber + 1);
// console.log(normalNumber + 2);
// console.log(normalNumber + 3);

// let bigNumber = 9007199254740991n;

// console.log(bigNumber + 1n);
// console.log(bigNumber + 2n);
// console.log(bigNumber + 3n);

// // Output:
// // 9007199254740992
// // 9007199254740992
// // 9007199254740994
// // 9007199254740992n
// // 9007199254740993n
// // 9007199254740994n

// // Explanation:
// // Number can safely represent integers only up to 9007199254740991.
// // Beyond this limit, Number may lose integer precision.
// // BigInt can represent very large integers with exact precision.



// // 7. Choose the Correct Type




// let uniqueId = Symbol("id");

// let largeInteger = 9007199254740991n;

// let uninitialized;

// let emptyValue = null;

// // Output:
// // uniqueId -> Symbol
// // largeInteger -> BigInt
// // uninitialized -> undefined
// // emptyValue -> null




// // Part g — Prediction & Fixing (3 Questions)

// // 8. Predict the Output


// let a;
// let b = null;
// let c = 42;
// let d = "Hello";
// let e = true;
// let f = Symbol("key");
// let g = 123n;

// console.log(typeof a, a);
// console.log(typeof b, b);
// console.log(typeof c, c);
// console.log(typeof d, d);
// console.log(typeof e, e);
// console.log(typeof f, f);
// console.log(typeof g, g);

// // Output:
// // undefined undefined
// // object null
// // number 42
// // string Hello
// // boolean true
// // symbol Symbol(key)
// // bigint 123n

// // Explanation:
// // a is undefined because it has no assigned value.
// // b is null, but typeof null returns "object".
// // c is a number.
// // d is a string.
// // e is a boolean.
// // f is a Symbol.
// // g is a BigInt.


// // 9. Fix the Code


// let num = 10;
// let text = "Hello";
// let flag = true;
// let empty;
// let nothing = null;
// let unique = Symbol("id");
// let big = 9007199254740991n;

// console.log(num);
// console.log(text);
// console.log(flag);
// console.log(empty);
// console.log(nothing);
// console.log(unique);
// console.log(big);

// // Output:
// // 10
// // Hello
// // true
// // undefined
// // null
// // Symbol(id)
// // 9007199254740991n


// // 10. Primitive vs Non-Primitive


// // a) 
// // Primitive data types store a single simple value.
// // Non-Primitive data types can store collections of values
// // or more complex structures.

// // Example of Primitive:
// let age = 18;

// // Example of Non-Primitive:
// let student = {
//     name: "Ayush",
//     age: 18
// };


// // b)
// // They are called primitive because they represent basic,
// // single values and are not objects themselves.

// // Examples:
// let number = 10;
// let word = "Hello";
// let status = true;
// let value;
// let nothingValue = null;
// let id = Symbol("id");
// let bigValue = 100n;


// // c)
// // An Object is a non-primitive data type.
// // It can contain multiple values as properties.

// // Example:
// let person = {
//     name: "Ayush",
//     age: 18,
//     city: "Ranchi"
// };

// // Output:
// // person is an Object.
// // It can store multiple related values together.









