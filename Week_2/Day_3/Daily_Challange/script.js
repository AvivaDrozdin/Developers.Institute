let x,y,z;

for(x=0; x <=6; x++){//run loop when x is <= 6, each loop add 1

    for (y=0; y < x; y++){ //nested loop. as long y is smaller than x, run loop add +1

        z=z+("*");  //Nested. Make z to z*
    } 
    console.log(z); //because we only want to see *
    z="";
} 

