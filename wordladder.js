const form = document.querySelector("form")
const NUM_BOXES = 6;

for (let i = 0; i < NUM_BOXES; i++) {
    let input = document.createElement("input")
    if (i != 0) {
        input.setAttribute("disabled","disabled");
    }
    input.setAttribute("maxlength", "5");
    input.setAttribute("pattern", "[A-Za-z]*");
    input.setAttribute("type", "text");
    input.setAttribute("size", "10");
    form.append(input);
}

const inputs = document.querySelectorAll("input");
inputs[0].focus();

for (let i = 0; i < NUM_BOXES; i++) {
    let input = inputs[i];
    input.addEventListener("keypress", (event)=> {
        if (event.key === "Enter" || event.keyCode === 13) {
            guess = input.value.toUpperCase();
            answer = document.getElementById("endWord").innerHTML;

            if (guess === answer) {
                input.style.backgroundColor = "lightgreen";
            }
            else if (i+1 < NUM_BOXES) {
                let next = inputs[i+1];
                next.removeAttribute("disabled");
                next.focus();
                input.style.backgroundColor = "lightgray";
            }
            else {
                input.style.backgroundColor = "lightcoral";

            }
            input.setAttribute("disabled","disabled");
        }
    });


}


/*
const inputs = document.querySelectorAll("input");
for (let input of inputs) {
    console.log(input.value);
}
*/