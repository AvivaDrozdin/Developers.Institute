function notBad(sentance){  //turns notBad into a specific function

    let not = sentance.indexOf("not");  //searches for index of NOT
    let bad = sentance.indexOf("bad"); //searches for index of BAD

    if(not>-1 && bad>-1 && bad > not){ 
      return sentance.substring(0, not) + "good" + sentance.substring(bad + 3);
    }
    return sentance;
  }
  
  console.log(notBad('This dinner is not that bad!'));
  console.log(notBad('This movie is not so bad!'));
  console.log(notBad('This dinner is bad!'))