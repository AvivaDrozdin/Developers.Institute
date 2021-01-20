// EXERCISE XP


// Exercise 1

// instruction (global variable)

// let age = prompt("What is your age?"); // Non needed since we have it in function!!!!


// declare function (local scope)
function checkDriverAge(age){ // if () is empty - argument also empty. if (age) has e.g. age - agrument needs an age
    if (age < 18){
        console.log("Sorry you're too young to drive this car")

    }else if (age > 18){
        console.log("Enjoy your ride")

    }else {
        console.log("Congrats on your first year of driving")
    }
}
//Call / Invoke the function
//checkDriverAge(prompt("What's your age?"))



//Exercise 2 

// Given a total due and an array representing the amount of change in your pocket, determine whether or not you are able to pay for the item.
// Change will always be represented in the following order: quarters, dimes, nickels, pennies.

// Quarters  = 0.25
// Dimes = 0.10
// Nickels = 0.05
// Pennies = 0.01






//Exercise 3


//create function to find multiplies

function multiples (){ //Exercise doesnt ask for parameter

    //create array to hold numbers
    let arrayNumber = []; // [0, 23, 46, 69, 92, 115, 138, 161, 184, 207, 230, 253, 276, 299, 322, 345, 368, 391, 414, 437, 460, 483]


    // create variable for the sum
   

    //loop through range of nr from 0 - 500
    for (number = 0; number <=500; number++){

        //check if nr devisible by 23
        if (number % 23 == 0){

            //if yes, ous to array
            arrayNumber.push(number)

        } else {
            //else continue running loop
            continue;
        }
    }
    return arrayNumber;   // return used to RETRIEVE the arrayNr to use in other functions. Makes local accessible in global
} 

multiples()


// function to find sum of multiplies

function sumNumbers () {

    //make new variable (x) - we need to access first function
    let  listNumbers = multiples() // return function attaches arrayNr to multiples(). If we use multiples() we basically use arrayNr.
    // Not listNumbers = multiple() = arrayNr

    //create new variable where to put the sum
    let sum = 0

        //make new counter - will become the sum
    for (i = 0; i < listNumbers.length; i++){ //create a loop to sum all the numbers together of the array

        sum += listNumbers[i] //sum is equal to list nr

    }  
    console.log(`The sum is ${sum}`)
}

sumNumbers()



// Exercise 4: 






//Exercise 5
shoppingList = ["Banana", "orange", "apple"]


let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 




function myBill(){

    let cost = 0; // cost of items inside basket
    
    for (let i = 0; i < shoppingList.length; i++) {
      let itemName = items[i]; // get the name of the for each item inside shopping list

      let itemPrice = cart[itemName]; // get the price for the each item
      sum += Number.parseFloat(itemPrice); // convert the price to a float and add it to the sum (parseFloat = Parses the argument as a float number and returns it. The argument is a string)
    }
    return sum;
  }

myBill();




//Exercise 6; 


