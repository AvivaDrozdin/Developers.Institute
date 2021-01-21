let x = 99; // x = 99 beers

let y = 1; // y = how many beers we take off

while(x>0){ // while there are more beers on the wall

    console.log(x+" bottles of beer, on the wall! " + x+ " bottles of beer! You take it down, you pass it around, you got " + x+ " bottles of beer on the wall" ) // show this

    if(x<y){ // condition for if there are less beers that there is demand
        x = x - x // Solution for when there are more beers to take away than available
    }else {
        x = x - y;
        y++ // increase the amount of beers subtracted
    }
}

console.log( x + "bottles of beer on the wall");