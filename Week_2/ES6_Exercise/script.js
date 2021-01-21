// Exercise 1

var num = 8;
var num = 10;
console.log(num); 
//expected outcome 10 / real outcome 10
//explanation. second var was reassigned with 10


//Exercise 2 (???)
function numbers() {
    for (var i = 0; i < 5; i++) {
      console.log(i);
    }
      console.log(i);
  }
  numbers();
  

//Exercise 3
//Which type of variable to use

//1.Create a global variable that save the amount of money you have in your account 
let myAccount = [200, 500, 1000, 50, 60, 190]

function income (){
    let income = []
    for (number = 0; number <=500; number++){
        myAccount.push(number)
        return myAccount;
    }
}
    
function incomeSum () {
    let total = income ()
    let sum = 0
    for (i = 0; i < total.length; i++){
        sum += total[i]
    } console.log(`The total on your account is ${sum}`)
}

incomeSum ()

             


//2. Create a variable that saves the amount of VAT





//3. Create a variable that saves the amount of all the expenses and revenue you did /received for the past last month


//4. Create a JS code that multiplies of the expenses by the VAT



//5. Create a JS code that changes the amount of the money you have in your account depending on your expenses/revenue.



//6. Display it

let 