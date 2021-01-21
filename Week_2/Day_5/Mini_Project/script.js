let display = document.getElementById("display"); // html source

let arr = [];    // make new empty array to push our signs into

function my_f(sign){ //new function - same name as my signs
    arr.push(sign); // we push each sign into the array
    console.log(arr);
    let str = arr.join('');
    display.innerHTML=str;
}

function calculate(){ //new function to calculate our arrow
    let str = arr.join(''); // new variable str that joins our array together
    console.log(str);

    let calc = eval(str); // new variable calc that calculates our variable str (that has the array inside)
    console.log(calc);  
    display.innerHTML=display.innerHTML+'='+calc;
}

function reset(){           // create a reset button to clear all of the data.
    arr = [];
    display.innerHTML=''
}
function backspace(){
    arr.pop();
}














