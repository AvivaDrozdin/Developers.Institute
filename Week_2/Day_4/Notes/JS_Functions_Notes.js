//When you have a big task: devide task in functions
// e.g I want to send email to my users that I have a sale

// 1. First function retrieves data from database
// 2. Second function retrieves emails
// 3. Third function sends the email


//Local Scope  = variables within (functions) "Home"
// Global Scope = variables anywhere in code "Park"

//---> You can go from Home to Park and pick a flower, but someone from the park can't just come into your home


// Functions assign a specific task!


        //nameOfFunction (parameter)
function greet(username, lastname){ //parameter name is username. Not accessible outside function
    console.log(`Hello ` + username + lastname); //Displays Hello and name of user - Username will be displayed in argument
}

// Invocating / calling the function

//function (argument)
greet (`John`,`Johnson`);  // Should show Hello John Johnson
greet (`Mary`) // Should show Hello Mary undefined - because we didn't define lastname argument


//EXAMPLE: We want to display mums age (whos 2x my age) & dads age (1.2 x mums age)

function familyAge (myAge){
    let mumAge = myAge*2 // local variable mumAge
    let dadAge= mumAge*1.2 // local variable dadAge
    console.log(`My Mums age is ${mumAge} and my Dads age is ${dadAge}` )
} 

familyAge (25)



// RETURN:
//if I want to return specific value of parameter

function totalAge (myAge2){
    let ageMum = myAge2*2 // local variable mumAge
    let ageDad= ageMum*1.2 // local variable dadAge
    return ageMum+ageDad;
} 

totalAge (30)




// Overriding: 

function speak (name = "David", time = "night"){
    console.log(`Good ${time} ${name}`);
}

speak("Mario", "day") // this overrides top an becomes food day mario

speak ("Alex") // because we didn't define time argument it will take night argument from top




