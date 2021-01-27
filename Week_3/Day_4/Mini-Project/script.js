// STEP 1) create Sidebar clear button & divs (21)
// access container & sidebar div
// let sidebar = document.getElementById('sidebar') 


let sidebar = document.getElementById('sidebar')
//console.log(sidebar);


// create Clear Button
let btn = document.createElement('button');
btn.setAttribute('id', 'button')
btn.innerHTML = 'Clear';

btn.addEventListener('click', clear) //set button attribute to onclick - execute function clear

sidebar.appendChild(btn);


// create color divs
let colors = ['red', 'orange', 'yellow', 'yellowgreen', 'lightgreen', 'green', 'turquoise', 'cyan', 'lightblue', 'dodgerblue', 'blue', 'darkblue', 'rebeccapurple', 'indigo', 'darkmagenta', 'fuchsia', 'violet', 'pink', 'lightgrey', 'white', 'black']



for (let i = 0; i < colors.length; i++){
    let newDiv = document.createElement('div');
    newDiv.className = 'color';
    newDiv.addEventListener('click', choose) // add attribute to execute "choose" function on click
    newDiv.style.backgroundColor = colors[i];
    sidebar.appendChild(newDiv)
    
}

function choose (event){
    console.log(event.target.style.backgroundColor); // selects the color 
    let colorSafe = event.target.style.backgroundColor;
}





// create colorgrid divs
let colorgrid = document.getElementById('colorgrid')

    for (let i = 0; i < 4500 ; i++){
        let newDiv = document.createElement('div');
        colorgrid.appendChild(newDiv)
        newDiv.className = 'grid';
        newDiv.addEventListener('mousedown', paint)
        newDiv.addEventListener('mousover', paint)// add attribute to execute "color" function on click

}


let colorDiv = null; // Empty variable for color in div
let mousedown = false; // Boolean for mousedown event
let sidebarColor = 0; // initialising element for loop
let gridFill = 0; // initialising element for loop
let clearUp = document.getElementById('button');
let colorsInSidebar = document.querySelectorAll('#sidebar > div');
let grid_fills = document.querySelectorAll('#colorgrid > div');
let body = document.getElementsByTagName('body')[0];

clearUp.addEventListener("click", clear); // clears the creen by clicking the button and calling the function bellow

function clear () {
    for (grid_fill of grid_fills) {
        grid_fill.style.backgroundColor = "white";
    }
}

body.addEventListener("mousedown", function(){
    mousedown = true;
}); // checks for boolean of mouse down status

body.addEventListener("mouseup", function(){
    mousedown = false;
}); // checks for boolean of mouse down status


    function paint (event){
        console.log(event)
    }




