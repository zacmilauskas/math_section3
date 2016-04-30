// tell jasmine where to find our code
var math = require ('../math');

describe ("A program that does basic artithmetic", function() {
 it ("can add two numbers together", function() {
 	expect(math.add(3,5)).toBe(8);
 });

describe ("A program that does basic subtraction", function() {
 it ("can subtract two numbers together", function() {
 	expect(math.sub(3,5)).toBe(-2);
});

describe ("A program that does basic multiplication", function() {
it ("can multiply two numbers together", function() {
 	expect(math.multiply(3,5)).toBe(15);
});

});
