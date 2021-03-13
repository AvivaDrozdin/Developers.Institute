body = document.querySelector('body')

function makeblue(){
    body.className = 'blue'

}

function makered(){
    body.className = 'red'
}

function makegreen(){
    body.className = 'green'
}


// run function after 3000ms
// also known as callback function
setTimeout(makeblue, 1000) 
setTimeout(makered, 2000)
setTimeout(makegreen, 3000) 

// doesn't wait until one function executed, starts counting ms at same time - that why there is only 1sec between color changes