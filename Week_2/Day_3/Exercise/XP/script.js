//EXERCISE 1

let colors =["Blue", "Red", "Green", "Yellow"];
let suffix =["st", "nd", "rd", "th"]; //BONUS

for (let i =0; i<colors.length; i++){
    console.log("My #" + (i+1) + " " +  "choice is" + " " + colors[i]) 
}

//bonus 
for (let i =0; i<colors.length; i++){
    console.log("My " + (i+1) + (suffix[i]) + " " +  "choice of color is" + " " + colors[i]) 
}


// EXERCISE 2

//1.
let people = ["Greg", "Mary", "Devon", "James"];

for (let person of people){
    console.log(person);  //should display the names
}

//2.

people.splice(0,1); // starts at postition 0 , splices off 1
console.log(people);


//3.
people.splice(2,1,"Jason"); //starts off at position 2, cuts off 1 item, adds Jason
console.log(people);

//4.
people.push("Aviva"); //pushes aviva to end
console.log(people);

//5.
for (let person = 0; person < people.length; person++){
    if (people[person] == "Jason"){
        break;
    } 
    console.log(people[person])
}


//6.
let newPeopleArray = [];  //create new array
for (person of people) {  // start running loop
    if (person != 'Mary') //if persons are NOT mary
    newPeopleArray.push(person) //push person to newPeopleArray
}
console.log(newPeopleArray);



//EXERCISE 3

// let number = prompt("Give me a number!")

// number = 10; // x equals to 0

// do {  
//     number++;  //DO add x +1
//     prompt("New Number pls"); // display console.log ("x=" + x)
// }while (number <10) // While x is smaller than 5



//EXERCISE 4

let guestList = {
    Randy: "Germany",
    Karla: "France",
    Wendy: "Japan",
    Norman: "England",
    Sam: "Argentina"
}

for (let person in guestList){
    console.log("Hi I'm" + " " + person + " " + "from" + " " + (guestList[person]));
}


//EXERCISE 5

let family = {
    "size": 3,
    "residence": "germany",
    "origin": "lithuania"
}
//only properties
for (let elements in family){
    console.log(elements);
}

//only value ?? 
console.log(family[elements]);

    


//EXERCISE 6
let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"] 

names.sort();
console.log(names);

let SecretName = names.map(x => x[0]).join('');

// console.log(SecretName);