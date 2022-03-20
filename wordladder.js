// Create boxes
const form = document.querySelector("form")
const NUM_BOXES = 6;
const WORD_LENGTH = 5;
const boxes = createGameBoxes(form,NUM_BOXES);
const messageContainer = document.getElementById("message-container");

// Enable first box
boxes[0].removeAttribute("disabled");
boxes[0].focus()

// Check guess
for (const box of boxes) {

    box.addEventListener("keypress",(event)=> {

        // Check answer when user presses "Enter".
        if (event.key === "Enter" || event.keyCode === 13) {

            let isValid = validateGuess(box);
            if (isValid) {
                processGuess(box);
            }
            else {
                box.value = "";
            }
        }
    });
}


// *** HELPER FUNCTIONS *** //

function createGameBoxes(form,n) {
    
    for (let i = 0; i < n; i++) {

        let box = document.createElement("input")
        box.setAttribute("maxlength", WORD_LENGTH);
        box.setAttribute("onkeypress", "lettersOnly(event)")
        box.setAttribute("type", "text");
        box.setAttribute("size", "10");
        box.setAttribute("disabled","disabled");

        form.append(box);
    }

    return document.querySelectorAll("input")
}

function lettersOnly(event) {

    let char = String.fromCharCode(event.which);

    if(/[^A-Za-z]/.test(char)) {
        event.preventDefault();
    }
}


function validateGuess(box) {

    let guess = box.value;
    let time = 2000; // ms
    let message = "";

    if (guess.length < WORD_LENGTH) {
        message = "NOT ENOUGH LETTERS";
    }

    if (guess.length > WORD_LENGTH) {
        message = "TOO MANY LETTERS";
    }

    if (guess.match(/[A-Za-z]/g) === guess.split("")) {
        message = "ONLY LETTERS ALLOWED";
    }

    // TODO: WORD NOT IN WORD LIST    

    // TODO: WORD MUST DIFFER BY ONE LETTER

    if (message) {
        box.setAttribute("disabled","disabled");
        displayMessage(message,time);
        box.removeAttribute("disabled");
        return false
    }

    return true; 

}


function displayMessage(message,time) {

        const para = document.createElement("p");
        para.classList.add("message-box");
        para.innerHTML = `${message}`;

        messageContainer.appendChild(para);
        para.classList.add("fadeOut");
        
        setTimeout(() => {
            messageContainer.removeChild(para);
        }, time);
}


function processGuess(box) {

    // Win: Correct guess.
    guess = box.value.toUpperCase();
    answer = document.getElementById("endWord").innerHTML;
    if (guess === answer) {
        box.style.backgroundColor = "lightgreen";
    }

    // Loss: Incorrect guess on last box.
    else if (box === form.lastChild) {
        box.style.backgroundColor = "lightcoral";
    }

    // Continue: Incorrect guess. Move to next box.
    else {
        box.style.backgroundColor = "lightgray";
        let nextBox = box.nextSibling;
        nextBox.removeAttribute("disabled");
        nextBox.focus();
    }

    // Disable box.
    box.setAttribute("disabled","disabled");
}


