let age = prompt("What is your age?"); //sends prompt to ask for age
console.log(age)

if (Number(age) < 18) {
    alert("Sorry, you are too young to drive this car. Powering off");
} // if age below 18 - alert - can't drive

else if (Number(age) > 18) {
    alert("Powering On. Enjoy the ride!");
} //if age above 18 - alert power on

else if (Number(age) == 18) {
    alert("Congratulations on your first year of driving. Enjoy the ride!")
}  // if value is exactly 18 - prompt message above

