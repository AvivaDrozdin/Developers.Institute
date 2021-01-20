 let sentence = prompt("words sep by comma", "daniel, marry, james, elizabeth") // ask people to add words like "daniel, marry, james, elizabeth""

 //console.log(sentence);

 let arr = sentence.split(", "); // make new variable to put our names into an array

 // console.log(array);

 let longest = 0 //make a new variable named longest that is empty

 for (let i = 0; i < arr.length; i++){ //we run a loop, starting at i being 0 and running as long as it's value is smaller than the length of the array (= we run through the entire length of the array)

     if (arr[i].length > longest){ // if i (which is one of the names now) of the array is now bigger than longest (which is empty) 

         longest = arr[i].length // longest becomes the length of arrays i (which is one of the names)
        
     } 
 }

 for (let i = 0; i <= arr.length; i++){ // we run a loop for i ???

     if ((i==0) || (i == arr.length)){ // IF i == to 0 or to the array length we 

         console.log("*".repeat(longest+4)) // we run console log of * and repeat our variable longest+4 (for extra space)

         continue; // then we continue our loop so it goes through the entire array length
     }
     console.log(`* ${arr[i]}${" ".repeat(longest-arr[i].length)} *`) //console logs makes * + arr[i]?? + " " + repeats length og: longest name - arr[i] + * 
 } 




