let language; //variable language
language = prompt("Do you speak French, English or Hebrew?") //promts to type in what language you speak
switch (language) //switches language 
{
    case "French": //in case of french
        alert("Bonjour"); //to bonjour
        break; 
    case "English": //in case of english
        alert("Hello"); //to hello
        break;
    case "Hebrew": //in case of hebrew
        alert("Shalom"); //to shalom
        break;
    default: //in case of anything else
        alert("01110011 01101111 01110010 01110010 01111001"); //to this
        break;
}







