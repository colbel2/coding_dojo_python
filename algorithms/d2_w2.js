// parensValid(str) - takes in one argument, a string. returns true if the
// parentheses in the string are valid and false otherwise.
// "a(z)g" - true
// ")sadf(" - false
// what's valid?
// - no more opening than closing parens and vice versa
// - every opening paren has a matching properly located closing paren
// - we can ignore all non-paren characters


function parensValid(str) {
    let i = 0;
    

console.log(parensValid("hello!") === true);
console.log(parensValid("a(z)g") === true);
console.log(parensValid("12;(d-[)](qwg)a") === true);
console.log(parensValid(")sadf(") === false);
console.log(parensValid("addToFront(7, [1, 6, 2, 9']") === false);
console.log(parensValid("(()())(()()()))") === false);