let bodyBackground = document.body.firstElementChild;
bodyBackground.style.backgroundColor = '#bde0fe';

// 2. Don't display the first name (John) in the list & add a border to the second name (Pete).

document.body.children[1].firstElementChild.innerHTML = "";

document.body.children[1].lastElementChild.style.border = "1px solid black";

// 3. Change the font size of the whole body.

document.body.style.fontSize = "50px";


