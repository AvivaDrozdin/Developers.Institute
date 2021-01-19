// LOOPS

//FOR Loop - To do the same action x amout of times


for (let counter = 1; counter <= 4; counter++){
    console.log("the loop runs, counter: ", counter)
}

// counter = 1  counter starts at 1
// if counter is smaller OR equal to 4 - run action + add 1
// counter now runs at 2, <= 4, run action, +1
// counter at 3, <= 4, run action, +1
// counter at 4, <=4, run action, +1
// counter at 5 IS NOT smaller or equal to 4 = STOP ACTION


// BREAK OUT OF LOOP (usually used with IF)
for (let counter = 1; counter <= 4; counter++){
    console.log("the loop runs, counter: ", counter);

    if(counter ==2){  // IF condition is true (counter  equals to 2)
        console.log("Yeah") // console.log displays "Yeah"
        break; // and breaks out of the loop.
    }
} 

// SKIP INSIDE LOOP (usually used with IF)
for (let counter = 1; counter <= 4; counter++){ 
    if(counter ==2){ // IF condition is true (counter equals to 2)
        console.log("Yeah") // console log displays "Yeah"
        continue; // and continues on with the remaining counter
    }
    console.log("the loop runs, counter: ", counter);
}


// LOOP inside Array

let colors = ["blue", "yellow", "red"]
console.log(colors) // will loop with , inbetween. So what to do?

// Possible: But repetetive
console.log(colors [0], colors [1], colors [2]) 

//Avoid repetition with FOR LOOP:
for (let counter =0; counter <=2; counter++) // Will run 3x
console.log(colors[counter])

// 1st loop: counter = 0 --> colors [0]
// 2nd loop: counter = 1 --> colors [1]
// 3rd loop: counter = 2 --> colors [2]


// IF DON'T KNOW HOW MANY TIMES I WANT TO RUN IT? / WHAT END OF ARRAY IS?

                        //colors.length = run loop until reach end of colors
for (let counter =0; counter <colors.length;  counter++) // 
console.log(colors[counter])





// FOR IN & FOR OFF 

// How to loop through everythin in the object Person?
let myObjects = {
    "obectsProperty" : "propertyValue"
}
 
//e.g
let person = {
    "fname": "Aviva",
    "lname": "Drozdin",
    "arms": 2
}

// USE FOR IN!= for(looking at property IN object)

    // let "GiveAnyName" in object "person"
for (let i in person){
    console.log(elements);  //should display fname, lname, arms
    console.log(person[elements]) // = property name + proeprty value = fname aviva
}


// LOOP OFF (don't work on Objects! only strings and arrays)

//e.g
let colors = ["blue", "green", "yellow"]

// USE FOR OFF!= of(looking at value OF object)

    // let "GiveAnyName" in object "person"
for (let elements of colors){
    console.log(elements);  //should display blue, green, yellow
    console.log(person[elements]) // 
}

if using array of people use let person! 




// WHILE LOOP 
// Used when don't know end point: often used when required user input 

let x = 0; // x equals to 0

while (x < 3) { // while x smaller than 3?

    x++ // add +1

    console.log(x)  
} // and continues until reaches 3


// !!!!!! CAREFUL OF ENDLESS LOOP !!!!
let x = 0;

while (x < 3) { // while x smaller than 3

    x++ // if there is NO! condition - will run forever & crash!!!!!

    console.log(x)  
} // and continues until reaches 3






// DO WHILE LOOP

let x = 0; // x equals to 0

do {  
    x++;  //DO add x +1
    console.log ("x=" + x) // display console.log ("x=" + x)
}while (x <5) // While x is smaller than 5

