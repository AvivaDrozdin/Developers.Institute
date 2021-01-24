// Exercise 1

// Part 1. (Plan: access body - access div - change name)
let navBar = document.getElementById('navBar') // accessing navbar
navBar.setAttribute('id', 'socialNetworkNavigation') // change navBar name


//Part 2. (Plan: access ul - access li - append text - append li)

let ul = document.getElementsByTagName('ul')[0] // access ul position OUTSIDE of ()!!! because we want first child outside the ul

let newLi = document.createElement('li'); // create li

let anchor = document.createElement('a'); // create a tag "logout":

let att = document.createAttribute('href'); // create href to the anchor

att.value = '#' //set our att value to #

anchor.setAttributeNode(att) //append anchor to att  = anchor href now has value #

let liText = document.createTextNode('Logout') //text node for li:

//APPEND
anchor.appendChild(liText) // append text to the anchor

newLi.appendChild(anchor) // append anchor to newLi

ul.appendChild(newLi) // add new li to UL

console.log(newLi);

