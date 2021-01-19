let sentence = "The dinner is not so bad";

let arraySentence = sentence.split(" ");

console.log(arraySentence);



let notIndex = arraySentence.indexOf("not");
let badIndex = arraySentence.indexOf("bad");

console.log(arraySentence);

let wordCounts = badIndex-notIndex+1

if (notIndex < badIndex) {
  arraySentence.splice(notIndex, wordCounts, "good")
  console.log(arraySentence.join(" "))
}



