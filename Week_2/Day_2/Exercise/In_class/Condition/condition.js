// CONDITIONS 

// II means OR
// && means AND

// Exersise Bank

//let bankAmount = 10;

//if my bankamount is equal or larger than 500
//if (bankAmount >= 500){
    //if condition true should get following sentence:
//    console.log("I can buy a computer"); // IF Only runs if conditions are true. If condition false - USE ELSE
//}  else {
    //will run only if condition false
//    console.log("You can't afford it")
    
//}
    
    
// Birthday exercise

//let age = 18
//let birthday = true

//if (age ==18 && birthday == true){ //IF condition is 
//    age = age + 1
    //runs if true
//    console.log("age"+ age ) //If condition false goes to else if
//} else if (age == 100){
    //runs if true
//    console.log("congratulations") //if this is ALSO false goes to else
//}
//else {
    // runs if false (Not always needed)
//    console.log ("it's not your birthday")
//} 


// TRY OUT
let username = "David"

if (username == "Lea") {
        console.log(username)
} else if (username == "Dave"){
    console.log(username)
} else {
    console.log("You are not David")
}



// SWITCH CASE 

// Used to check if an one element is == to other element

let fruit = 'Papayas'; // we want to check if papaya == 

switch (fruit) {
  case 'Oranges':
    console.log('Oranges are $0.59 a pound.');
    break; //getting out of switch
  case 'Papayas':
    console.log('Papayas are $2.79 a pound.');
    // expected output: "Mangoes and papayas are $2.79 a pound."
    break; //getting out of switch
  default:
    console.log('Sorry, we are out of ' + fruit + '.');
}

console.log("after switch")

//if fruit != to oranges, goes to case:"papaya". if true: displays conole.log("papayas are ...."). 
//if fruit also false for papaya goes to default (sorry out of fruit)

// If using OR - one can be true and one false. if using AND both have to be true

//after the break; goes to console.log ("after switch")




