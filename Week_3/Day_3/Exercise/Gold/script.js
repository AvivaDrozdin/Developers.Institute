let letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];


for (let i = 0; i < letters.length; i++) {
    let newSpan = document.createElement("span");
    let newContent = document.createTextNode(letters[i]);
    newSpan.appendChild(newContent);
    newSpan.className = ('box');
    newSpan.setAttribute('draggable', 'true')
    document.body.appendChild(newSpan);
    newSpan.style.margin = '10px'
    newSpan.style.padding = '5px'
    newSpan.style.border = '2px solid black'

    newSpan.addEventListener("dragstart", dragItem) // Keeps showing error (not a function)
    newSpan.addEventListener("dragend", dropItem)

    function dragItem(event){
        console.log(event.clientX);
    };

    function dropItem(event){
        let horizontal = event.clientX
        let vertical = event.clientY
        event.target.style.left = horizontal+'px'
        event.target.style.top = vertical+'px'
        event.target.style.position = 'absolute'
        console.log(horizontal)
    };


}


 



