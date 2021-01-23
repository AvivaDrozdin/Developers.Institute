// EXERCISE XP
// Exercise 1

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
// checkDriverAge(prompt("What's your age?")) // commented out to avoid prompt each time website reloads





//Exercise 2 

// Given a total due and an array representing the amount of change in your pocket, determine whether or not you are able to pay for the item.
// Change will always be represented in the following order: quarters, dimes, nickels, pennies.

let myWallet = {
    Quarters: 0.25,
    Dimes: 0.10,
    Nickels: 0.05,
    Pennies: 0.01
}
function change([quarter, dime, nickel, penny], pay) {
    let total = quarter*myWallet.Quarters + dime*myWallet.Dimes + nickel*myWallet.Nickels + penny*myWallet.Pennies;
    if (pay <= total) {
        return "true"
    } else {
        return "false"
    }
}

let enough = change([25, 20, 5, 0], 4.25);
console.log(enough);





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






// Exercise 4 
let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}
// Create a function called checkBasket().
function checkBasket() {


// ask the user for the item he wants
let itemRequest = glasses  //prompt("What item do you want?")
// and let him know if it's in the basket or not
// Hint: Use the in keyword inside the conditional
  if (itemRequest in amazonBasket){
    console.log(`You already have ${Object.amazonBasket[]} + ${amazonBasket} in your cart`)
  }
}





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

// John & Fam went to 3 different families

// Tip calculator 
// IF bill <50 = tip 20%
// IF bill 50-200 = tip 15%
// IF bill >200 = 10%

function tips (amount){
    let tipSum = [];
    let total = [];

    for (let i in amount){
        if (amount[i] <50){
            tipSum.push(amount[i] * 0.2);
            total.push(parseInt(amount[i]) + parseInt(amount[i] * 0.2));
        }
        if (amount[i] >=50 && amount[i] <200){
            tipSum.push(amount[i] * 0.15);
            total.push(parseInt(amount[i]) + parseInt(amount[i] * 0.15));
        }
        if (amount[i] >= 200){
            tipSum.push(amount[i] * 0.1);
            total.push(parseInt(amount[i]) + parseInt(amount[i] * 0.1));
        }
    }
    return tipSum + ' ' + result;
}

let totalBill =prompt("Enter your bills, separated by ,")

console.log(tips(totalBills.split(',')));





// EXERCISE 7 


//1.Define a function called hotel_cost()
let nights = ""
let price =0;
function hotelCost(){
    let test=false;
        while (test===false) {
            nights = prompt("How many nights are you staying?");
            if (Number.isInteger(parseInt(nights))) { //making sure the answer is only user when numerical
                test =true; 
                price = 140*nights;
            } else {
                test=false;
            }
        }
        return price;
}
console.log(hotelCost());


//2.Define a function called plane_ride_cost()
let city="";
let plane=0;
function plane_ride_cost() {
    let test2=false;
        while (test2===false) {
            city = prompt("Where arou you going?");
            if (typeof city === 'string') {
                test2 =true;
            } else {
                test=false;
            }
        }
        if (city == "London") {  
            plane=183;
        } else if (city=="Paris"){
            plane=220;
        } else {
            plane=300;
        }
        return plane;
}

 console.log(plane_ride_cost());

//3.Define a function called rental_car_cost().

let days=false;
let car=0;
function rental_car_cost() {
    let test=false;
        while (test===false) {
            days = prompt("How many days do you want to rent the car for?");
        
            if (Number.isInteger(parseInt(days))) { // ensures reply only used if numerical
                test =true;
            } else {
                test=false;
            }
        }
        if (days>10) {
            car = 40*days*0.95;
        } else {
            car=40*days;
        }
        return car;
}

// console.log(rental_car_cost());

//4.Define a function called total_vacation_cost() that returns the total cost of the user’s vacation depending on the 3 functions that you created above.
let totalCost = "";
function total_vacation_cost() {
    totalCost="The hotel cost : $"+hotelCost()+", The plane cost : $"+plane_ride_cost()+", The car cost : $"+rental_car_cost();
return totalCost;
}

console.log(total_vacation_cost());

    




