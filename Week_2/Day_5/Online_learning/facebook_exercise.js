let database = [
    {
        username: "maria"
        password: "super123"
    },

    {
        username: "david"
        password: "heLL0"

    },

    {
        username: "ingrid"
        password: "$ecretCode"

    }
];


let newsfeed = [
    {
        username: "roni"
        timeline: "Good Morning"

    },
    {
        username: "tom"
        password: "blablablaa"

    },
    {
        username: "ingrid"
        password: "hello world, it's me"

    }

];

function validUser(username.password) {
    for (let i =0; i < database.length; i++){
        if (database[i].username === username &&
            database[i].password === password){
                return true
            }
    }
    return false
}

    
function signIn(username,password) {
    if (validUser(username, password)) {
        console.log(newsFeed);
    } else {
        alert("Sorry wrong username or password")
    }
}

let userNamePrompt = prompt("What's your username?");
let passwordPrompt = prompt("What's your password?");

signIn(userNamePrompt, passwordPrompt)