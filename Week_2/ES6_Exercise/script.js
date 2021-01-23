// // Exerecise_1

var num = 8;
var num = 10;
console.log(num); // expected outcome 10 because last value overrides the previous one



// Exercise_2

function numbers() {
let i; // variable added without definition = undefined outside loop
 for (i = 0; i < 5; i++) {
     console.log(i);
 }
     console.log(i);
 }
 numbers();



//Exercise_3

let myAccount = 10000;
console.log(`Account before spendings: ${myAccount}`);

const vat = 0.19;
let expenses = 2500;
console.log(`Amount of expenses: ${expenses}. Tax is ${vat*100}%`);

let vatAmount = expenses*vat;

myAccount -= (expenses-vatAmount);

console.log(`Remaining after spendings: ${myAccount}`);