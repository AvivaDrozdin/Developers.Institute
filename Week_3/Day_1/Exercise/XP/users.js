// EXERCISE 2

// Part 1 

let ul = document.body.firstElementChild.nextElementSibling // access first ul

let li = ul.lastElementChild // access first li


let liTwo = document.getElementsByTagName('li')[1].innerHTML='Richard'; // change name
console.log(liTwo);


// Part 2 + 3  (Change first to Aviva + Add new Li with Hey Student)

let collection = document.getElementsByTagName('li').length;   //grabbing all li to find out how many li we have
//console.log(collection);


let ulTwo = document.getElementsByTagName('ul'); // grab the ul

for (let selectedUl of ulTwo) { 
    selectedUl.firstElementChild.innerHTML = 'Aviva'
    let liNew = document.createElement('li');
    let text = document.createTextNode('Hey Students');
    liNew.appendChild(text)
    selectedUl.appendChild(liNew);
    //console.log(selectedUl.firstElementChild.innerHTML);
}


// Part 4 (Add to each UL new li saying "Hey Students");
let liFive = document.getElementsByTagName('li')[4];
    //console.log(liFive)

let secondUl = document.getElementsByTagName('ul')[1]
secondUl.removeChild(liFive);
console.log(liFive);


// Part 5 (Bonus)

for (let allUl of ulTwo) {
    allUl.setAttribute("class", "student_list")
}

ul.classList.add("university", "attendance");


