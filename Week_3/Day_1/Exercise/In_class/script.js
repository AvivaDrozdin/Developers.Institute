// How to access the div (from paper - rewrite later)

//Retrieve div
let bodyWebsite = document.body
let divWebsite = bodyWebsite.firstElementChild
                 // bodyWebsite.children[0]

// Retrieve ul
let ulWebsite = divWebsite.firstElementChild   

// Retrieve li (username)
let liThirdWebsite = ulWebsite.lastElementChild
                //ulWebsite.children[2]

console.log(liThirdWebsite)

//change name of li username
liThirdWebsite.textContent = "John" // changes "username" to "john"

//if want to access e.g sign up (second li - previous to username)
let liSecondWebsite = liThirdWebsite.previousElementSibling
console.log("Second li ", liSecondWebsite)