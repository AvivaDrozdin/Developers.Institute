 function wordFrameBuilder(sentence) { // we make a funktion to build a frame around sentance

     // let sentence = 'hello world in a frame';
     let sentenceArray = sentence.split(' ') // we split the sentence into separate strings
     // console.log(sentenceArray);

     let word = ''; //make a new local variable that is empty
     let longest = ''; // make another local variable that is empty

     for  (word of sentenceArray) { // we let a of loop run. To check vor values (word) OF the sentence array

         if (word.length > longest.length) { // IF word length is bigger than longest length (both are empty)
             longest = word; // longest becomes word
         }
     }


     let length = longest.length; //ne variable length made out of the length of longest (which is = word) = becomes lenght of longest word

     let stars = '' // new variable stars that is empty

     for (let i = 0;i < length; i++) { // we let a loop run and add +1 to it as long as it is smaller than length (see above) = longest word
         stars = stars.concat('*') // concat merges stars with * and makes new array (???)
     }
     // console.log(stars);
     let topAndBottom = '**' + stars +  '**'; //new variable topAndBottom = ** +stars (see above) + **
    // console.log(longest);



    // don't understand why this is repeating
     console.log(topAndBottom);
     for (word of sentenceArray) { //  // we let a of loop run. To check vor values (word) OF the sentence array again (????)
        let spaceLength = length - word.length; // new variable spaceLength = lenght (=length of longest word) - word.length (???)
        let space = ''; // new variable space that is empty
        for (let x = 0; x < spaceLength; x++) { //if x is smaller that spaceLength add +1 each loop
             space = space.concat(' ') // new variable of space that = to space with "  "
         }
         console.log('* ' + word + space + ' *');  // we console log * + 
     }
     console.log(topAndBottom);
 }
 wordFrameBuilder(prompt('please enter a sentence'))