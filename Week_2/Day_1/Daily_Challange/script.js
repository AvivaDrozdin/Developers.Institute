let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
console.log(fruits.length);

let removedFirst = fruits.splice(0,1); //removes 1 item = Banana index 0 (if use delete removedFirst makes an "empty" remark = deletes word but not the space it took )

let addedkiwi = fruits.push("Kiwi"); // Added Kiwi at the end

let removedFirstAgain = fruits.shift(""); // Removes Apple from first position

fruits.reverse(); // Reverses order of fruit

let moreFruit = ["Banana", ["Apples", ["Oranges"],"Blueberries"]];

console.log(moreFruit [1][1][0]); //moreFruit: First listed item in nisted = Apples index. First listed in next nisted = Orange [1] 


