// OBJECTS : access the element by the property
let user = {
    username: "John"
	password : 1234,
	email : "john@gmail.com",
	logIn : true,
	countries : ["israel", "usa"],
	friends : {
		names : ["David", "Sarah"]
	}
}
​

console.log(user);

// 1. display the friends nested object
console.log(user["friends"])
​
// 2. display the list of names of his friends
​console.log(user["friends"]["names"])

// 3. display the name of best friend : David
console.log(user["friends"]["names"][0])



let sentence = user["username"] + "best friend is" + user[["friends"["name"][0]]]