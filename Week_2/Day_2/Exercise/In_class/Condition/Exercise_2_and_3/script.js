// EXERCISE 2

let a = 2 + 2; //=4

switch (a) {
  case 3:
      // If a = 3 we will have alert "too small". Because case is false, goes to case 4
    alert( 'Too small' ); 
    break;
  case 4:
      // If a = 4 will get alert "exactly". Case 4 is true!
    alert( 'Exactly!' ); //expeceted outcome
    break;
  case 5: // if case a would have been false we'd be here
    alert( 'Too large' );
    break;
  default: // and if case 5 also false, we'd be here
    alert( "I don't know such values" ); 
}


// EXERCISE 3

let a = 2 + 2; //equals 4

switch (a) {
  case 4: //if a is equal to 4 alert prompt "right"
    alert('Right!'); //expected outcome
    break;

  case 3: // (*) grouped two cases  //if case 4 would be wrong we'd be here
  case 5:
    alert('Wrong!');
    alert("Why don't you take a math class?");
    break;

  default: // if case 3 and 5 also false, we'd be here
    alert('The result is strange. Really.');
}


