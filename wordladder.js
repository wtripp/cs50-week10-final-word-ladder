// Create boxes
const form = document.querySelector("form")
const NUM_BOXES = 6;
const boxes = createGameBoxes(form,NUM_BOXES);

// Enable first box
boxes[0].removeAttribute("disabled");
boxes[0].focus()

// Check guess
for (const box of boxes) {

    box.addEventListener("keypress",(event)=> {

        // Check answer when user presses "Enter".
        if (event.key === "Enter" || event.keyCode === 13) {
            checkGuess(box);
        }
    });
}


// *** HELPER FUNCTIONS *** //

function createGameBoxes(form,n) {
    
    for (let i = 0; i < n; i++) {

        let box = document.createElement("input")

        box.setAttribute("maxlength", "5");
        box.setAttribute("pattern", "[A-Za-z]*");
        box.setAttribute("type", "text");
        box.setAttribute("size", "10");
        box.setAttribute("disabled","disabled");

        form.append(box);
    }

    return document.querySelectorAll("input")
}


function checkGuess(box) {

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