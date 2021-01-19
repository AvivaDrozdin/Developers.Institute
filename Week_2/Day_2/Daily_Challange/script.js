function notBad(sentance){  //turns notBad into a specific function

  let not = sentance.indexOf("not");  //assigns "not" a part of sentance of indexOf(not)
  let bad = sentance.indexOf("bad"); //assigns "bad" a part of sentance of indexOf(bad)


  //If sentance includes variable not & includes variable bad and includes the word "bad" in this specific order; 
  if((sentance.includes("not"))&&(sentance.includes("bad"))&&(sentance.indexOf("bad"))){ 
    //returns: sentance extracts at start "not", ads good and extracts "bad"
    return sentance.substring(0, not) + "good" + sentance.substring(bad + 3);

  } //otherwise returns sentance as it was originally
  return sentance;
}

console.log(notBad("This dinner is not that bad!"));
console.log(notBad("This movie is not so bad!"));
console.log(notBad("This dinner is bad!"))