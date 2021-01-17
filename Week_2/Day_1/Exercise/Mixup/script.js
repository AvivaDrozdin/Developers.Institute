let string1 = "Mix ";
console.log(string1);

let string2 = "pod";
console.log(string2)

function mixUp(string1, string2) {
    return string2.slice(0, 2) + string1.slice(2) + " " + string1.slice(0, 2) + string2.slice(2);
  }
  console.log(mixUp('mix', 'pod'));


  