
# Assignment: Introduction to JavaScript
---

SECTION A – SHORT ANSWERS

Q1. JavaScript is a high-level programming language used to make web
pages interactive and dynamic.

Q2. JavaScript was created by Brendan Eich in 1995.

Q3. Its original name was Mocha. It was later called LiveScript and then
JavaScript.

Q4. No, JavaScript and Java are different languages. Java is mainly
class-based, while JavaScript is mainly prototype-based.

Q5. High-level means JavaScript is easy for humans to read and write and
hides many low-level computer details.

Q6. JavaScript is commonly called an interpreted language, but modern
engines also use JIT compilation to make it faster.

Q7. Chrome – V8 Firefox – SpiderMonkey Safari – JavaScriptCore

Q8. Dynamic typing means a variable can store different types of values
at different times without declaring its type first.

Q9. Static website shows mostly fixed content. Dynamic website can
change its content or behaviour based on users, data or actions.

Q10. HTML – gives structure to the webpage. CSS – gives style and
design. JavaScript – adds behaviour and interaction.

Q11. Frontend is the part the user sees and uses. Backend works behind
the scenes with servers, databases and application logic.

Q12. Node.js is a runtime that allows JavaScript to run outside the
browser, especially on servers.

Q13. ECMAScript is the standard/specification that defines how
JavaScript should work. JavaScript is an implementation of ECMAScript
with additional features.

SECTION B – TRUE OR FALSE

1.  False – JavaScript is dynamically typed.

2.  False – JavaScript can also run outside browsers using environments
    like Node.js.

3.  False – HTML gives structure. JavaScript is mainly used for
    behaviour and interaction.

4.  True.

5.  False – JavaScript is case-sensitive.

6.  False – name and Name are different variables.

7.  False – ECMAScript is a language standard/specification, not a
    programming language itself.

8.  False – React, Angular and Vue.js are mainly used for frontend
    development.

SECTION C – FILL IN THE BLANKS

1.  Brendan Eich, 1995

2.  HTML, CSS, JavaScript

3.  V8, SpiderMonkey

4.  Customer = Frontend user, Waiter = API, Chef = Backend

5.  .js

SECTION D – CONCEPTUAL QUESTIONS

Q14. Static website: Content is mostly fixed and changes only when the
code is changed. Example: a simple personal portfolio.

Dynamic website: Content can change according to users, data or actions.
Example: Amazon or a social media website.

Q15. 1. JavaScript responds to events like clicks, typing and mouse
movement. 2. It can change HTML and CSS without reloading the whole
page.

Q16. 1. Server-side development – Node.js 2. Mobile apps – React Native
3. Desktop apps – Electron 4. Game development – Phaser

Q17. JavaScript can be written directly inside an HTML file using
, or stored separately in a .js file and linked to HTML.

Advantages of external JS: 1. Code can be reused on many pages. 2. HTML
stays cleaner and easier to manage.

Q18. In a restaurant, the frontend is like the dining area and menu that
the customer sees and uses. The backend is like the kitchen where the
actual work is done. The waiter can be compared to an API because it
carries requests and responses between the customer and kitchen.

Q19. 1. JavaScript makes webpages interactive. 2. It is useful for
frontend and backend development. 3. It has many libraries and
frameworks. 4. It is widely used in web, mobile, desktop and other
applications. 5. It is a good foundation for learning modern web
development.

Section E: Code-Based Questions (3 Marks each)

Q20.<img width="727" height="243" alt="image" src="https://github.com/user-attachments/assets/927aff52-657a-465d-a544-b0c7ee5dbff5" />

Q21.<img width="1312" height="737" alt="image" src="https://github.com/user-attachments/assets/4483f5f2-e83b-4179-aa8d-fddaa503d02a" />

Q22.<img width="1017" height="587" alt="image" src="https://github.com/user-attachments/assets/808b47ac-e0cb-40c1-87ce-9cd3bc1a9e08" />

Section F: Practical / Application Based (5 Marks)
``` <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <h1>My First JavaScript Page</h1>

    <button onclick="changePage()">Click Me</button>

    <script>
        console.log("JavaScript is running successfully!");

        function changePage() {
            alert("Hello, B.Tech Student!");
            document.body.style.backgroundColor = "lightblue";
        }
    </script>

    
</body>
</html>

```








Section G: Higher Order Thinking (Bonus - 3 Marks)

Q24. JavaScript became popular because it is easy to learn, works in all major browsers, and has many libraries and frameworks. 
Node.js allowed JavaScript to run outside the browser, so it could also be used for backend and server-side development. 
ECMAScript updates added new features and improvements to the language. 
Because of this, JavaScript is now used for web, mobile, desktop, and many other types of applications.
