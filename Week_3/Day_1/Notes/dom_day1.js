// DOM contains a bunch of nodes where each node represents an HTML element.

// Root Elemet (Root Node)
//      |
//      |
//      v
// HTML Element (Child Node)
//      |
//      |
//      v
// Attributes/ Values (Leaf Node)



// DOm takes elements from HTML and makes them into Objects.
// Doing that it's able to modify them.



// HOW TO ACCESS FROM BODY? (e.g H1 "Hello")
document.body.children
// (accesses all children of <body> e.g <div>, <script> etc)
//lets say we only want to access the div to access it's children?
document.body.children[0] //gives me access to first child

document.body.children[0].children // accesses children of first child of body (children of the div)


// Changes made to HTML will be visible to user. 
// Changes made to CSS won't be visible to anyone apart fromme



// retrieving Id's 
let divWebsite = document.getElementById("Id name")
console.log("div: ", divWebsite)


// retrieve by class
let listWebiste = documet.getElementByClassName("classname")
console.log("list: ", listWebsite[]) // if want to reveive certain nr, use index nd like [0]

let listWebsite = document.getElementsByTagName(tag) //like li, will retrive all li's



// How to add new div/li/ul etc

// Step 1. Get to where we want to add the element
let bodyWebsite = document.body

// Step 2. Create
let newDiv = document.createElement("div")
// bodyWebsite.appendChild(newDiv) //adds new div at end of body

//Step 3. Add paragraph withing new div
let newPara = document.createElement("p")
let newCont = document.createTextNode("Hello new paragraph") // creating a new text node
newPara.appendChild(newCont) // add content to paragrapht

newDiv = appendChild(newPara) // add pargraph to div

bodyWebsite.appendChild(newDiv) // add div with para at end of body 



// add new ID or Class to the div: OPTION 1

// At Step 2
let newDiv = document.createElement("div")
newDiv.setAttribute("class", "newDiv") //adding a class to newDiv

// we can add images, classes, id, a tags etc.


// add new ID or Class to the div: OPTION 2 (better)
let newDiv = document.createElement("div")
newDiv.className = "giveClassName" //adds class with this name
newDiv.className = "oldDiv" // this OVERRIDES previous name-

//to have several classes:
newDiv.classList.add("new", "old", "className") // adds multiple classes to div


// HOW TO CHANGE CLASSES? 
//Toggle - if class existis it deletes. if it doesn't it adds

newDiv.classList.toggle("new", true) // REMOVES "new" class because it existis
newDiv.classList.toggle("superNew") //adds "superNew" class because it doesn't exist yet


// ACCESS STYLE?? - best to do in CSS tho

// option 1 (preferred)
newDiv.setAttribute("style", "background-color:red") 

// option 2
newDiv.style.backgroundColor = red




// What dom can be used for:
// If we want 5 pragaraphs we had to make them in html
//With DOM we can use a For Loop instead

for (let i = 0; i <5; i++){
    let newParagraph =document.createElement(p)
    newParagraph.className ="someClass"
    let newContent = document.createTextNode("Hello new paragraph")
    newParagraph.appendChild(newContent)
    newDiv.appendChild(newParagraph)
}
// This adds 5 new paragraphs with the text "hello new paragraph" with a class which we can now style



querySelector & querySelectorAll = CSS querySelector// can access all elements that for example are blue






