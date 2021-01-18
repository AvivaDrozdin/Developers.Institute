// ARRAY OF OBJECTS
let users = [
	{
		username : "John",
		password: 1234
	},
	{
		username : "Lea",
		password: 2222
	},
	{
		username : "David",
		password: 6767
	}
];

console.log(users);

// 1. display the information of the 2nd user (object)
console.log(users[1]);


// 2. display the password of the 2nd user
console.log(users[1]["password"]);