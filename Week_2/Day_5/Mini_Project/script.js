let display = document.getElementById("display"); // html source

let arr = [];    // make new empty array to push our signs into

function my_f(sign){ 
    arr.push(sign); 
    // console.log(arr);
    let str = arr.join('');
    display.innerHTML=str;
}

function calculate(){ //new function to calculate our arrow
    let str = arr.join(''); 
    // console.log(str);
    let calc = eval(str); 
    // console.log(calc);  
    display.innerHTML=display.innerHTML+'='+calc;
}

function reset(){           // create a reset button to clear all of the data.
    arr = [];
    display.innerHTML=''
}
function backspace(){
    arr.pop();
}














