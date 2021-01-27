let note = document.getElementsByClassName('note');

for (let i = 0; i <note.length; i++){
    note[i].onmouseover = function(event){
        event.target.classList.toggle('onnote');
    }
    note[i].onmouseover = function (event){
        event.target.classList('onnote');

    }
    note[i].onclick = function (event) {
        sound(event);
    }
}

document.body.onkeydown = function (event){
    sound(event);
}

function pressedLetter(letter){
    document.getElementById(letter).classList.toggle('playNote');
    setTimeout(function(){
        document.getElementById(letter).classList.toggle('playNote')
    }, 500);
}

function sound(event);
let audio = new Sound ();
if (event.target.id == 'a' || event.keycode == '65'){
    audio.src = 'tom.wav'
}
if (event.target.id == 's' || event.keycode == '83'){
    audio.src = 'boom.wav'