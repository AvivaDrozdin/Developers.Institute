let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let numberOfUsers= users.length;      //number of users as
let numberRemaining= numberOfUsers-2; // a string 

if (users.length ==0){  //if there are no item in the array / array empty
    console.log("no one is online"); // = no one is online

}else if (users.length ==1){ // if there is one item in the array / array has 1 user in list
    console.log(users[0] + "is online") // 1 user is online (Lea123 because index 0)

}else if (users.length ==2){ // if there are 2 item in the array / array has 2 users in list
    console.log(users[0] + " " + users[1] + "are online") // = 2 users online (Lea123 & Princess45 because ined 0 & index 1)

}else if (users.length >2){ //if there are MORE THAN 2 items in the array / more than 2 users in list
    console.log(users[0] + " " + users[1] + "and" + numberRemaining + "more are online") //2 users and numberRemaining(string) are online

}else{ // else I messed it up.
    console.log("Somethings wrong")
}
