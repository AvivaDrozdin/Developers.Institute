let word = "swiming"

if (word.length >= 3){
    console.log(word + "ing");

}else if(word.slice(0, -3) == "ing"){
    console.log(word + "ly");

}else if (word.length <3){
    console.log(word);

}else {
    console.log("SOS")
}

