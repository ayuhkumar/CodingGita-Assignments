// // 1. Personal Information


// let name = "Ayush";
// let age = 18;
// let city = "Ranchi";

// console.log(name);
// console.log(age);
// console.log(city);

// // Output:
// // Ayush
// // 18
// // Ranchi


// // 2. Change the Score


// let score = 50;

// score = 80;

// console.log(score);

// // Output:
// // 80


// // 3. Constant Value


// const PI = 3.14;

// console.log(PI);

// // Output:
// // 3.14


// // 4. Uninitialized Variables


// var num1;
// let num2;

// console.log(num1);
// console.log(num2);

// num1 = 10;
// num2 = 20;

// console.log(num1);
// console.log(num2);

// // Output:
// // undefined
// // undefined
// // 10
// // 20


// // 5. Choose the Correct Keyword

// const studentName = "Ayush";
// let marks = 75;
// const schoolName = "Oxford Public School";

// marks = 85;

// console.log(studentName);
// console.log(marks);
// console.log(schoolName);

// // Output:
// // Ayush
// // 85
// // Oxford Public School


// // 6. Understand Scope

// if (true) {
//     var a = 10;
//     let b = 20;
//     const c = 30;

//     console.log(a);
//     console.log(b);
//     console.log(c);
// }

// console.log(a);

// // console.log(b); // ReferenceError
// // console.log(c); // ReferenceError

// // Output:
// // 10
// // 20
// // 30
// // 10
// // b and c cannot be accessed outside the if block.


// // 7. Test Re-declaration


// var user = "Ayush";
// var user = "Rahul";

// console.log(user);

// // Output:
// // Rahul
// // var allows re-declaration.


// // The following code gives an error:
// //
// // let user = "Ayush";
// // let user = "Rahul";
// //
// // Output:
// // SyntaxError: Identifier 'user' has already been declared
// //
// // let does not allow re-declaration.


// // 8. Test Re-assignment

// var x = 10;
// let y = 20;
// const z = 30;

// x = 100;
// y = 200;

// // z = 300; // TypeError: Assignment to constant variable.

// console.log(x);
// console.log(y);
// console.log(z);

// // Output:
// // 100
// // 200
// // 30
// // var and let allow re-assignment.
// // const does not allow re-assignment.


// // 9. Predict and Explain


// var x = 10;

// if (true) {
//     var x = 20;
//     let y = 30;
//     const z = 40;
// }

// console.log(x);
// console.log(y);
// console.log(z);

// // Output:
// // 20
// // ReferenceError: y is not defined
// // ReferenceError: z is not defined

// // Explanation:
// // var is function-scoped, so the x declared inside the if block
// // refers to the same variable x and changes its value to 20.

// // let and const are block-scoped.
// // Therefore, y and z exist only inside the if block.
// // They cannot be accessed outside the block.


// // 10. Fix the Program
// // Fix the errors related to initialization, re-declaration,
// // re-assignment, and scope.

// const name = "Ayush";

// let age = 20;
// age = 25;

// if (true) {
//     var city = "Delhi";
//     let country = "India";

//     console.log(country);
// }

// console.log(city);

// const score = 50;
// let newScore = score;
// newScore = 80;

// console.log(name);
// console.log(age);
// console.log(newScore);

// // Output:
// // India
// // Delhi
// // Ayush
// // 25
// // 80

// // Explanation:
// // const variables must be initialized when declared,
// // so name is given a value immediately.

// // age is declared only once using let.
// // Its value is changed using re-assignment.

// // country is declared inside the if block,
// // so it must be accessed inside that block.

// // score is declared using const, so its value cannot be changed.
// // A new variable newScore is used when a changeable value is required.