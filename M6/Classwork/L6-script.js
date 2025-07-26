function getHistory() {
    return document.getElementById("history-value").innerText;
}

// Print to history
function printHistory(num) {
    document.getElementById("history-value").innerText = num;
}

// Get current output
function getOutput() {
    return document.getElementById("output-value").innerText;
}

// Print to output
function printOutput(num) {
    if (num === "") {
        document.getElementById("output-value").innerText = "";
    } else {
        document.getElementById("output-value").innerText = getFormattedNumber(num);
    }
}

// Format number with commas
function getFormattedNumber(num) {
    if (num === "-") {
        return "";
    }
    const n = Number(num);
    return n.toLocaleString("en");
}

// Remove commas from number
function reverseNumberFormat(num) {
    return Number(num.replace(/,/g, ""));
}

// Attach event listeners to operators
const operators = document.getElementsByClassName("operator");
for (let i = 0; i < operators.length; i++) {
    operators[i].addEventListener("click", function () {
        if (this.id === "clear") {
            printHistory("");
            printOutput("");
        } 
        else if (this.id === "backspace") {
            let output = reverseNumberFormat(getOutput()).toString();
            if (output) {
                output = output.slice(0, -1);
                printOutput(output);
            }
        } 
        else {
            let output = getOutput();
            let history = getHistory();

            if (output === "" && history !== "") {
                if (isNaN(history[history.length - 1])) {
                    history = history.slice(0, -1);
                }
            }

            if (output !== "" || history !== "") {
                output = output === "" ? output : reverseNumberFormat(output);
                history += output;

                if (this.id === "=") {
                    try {
                        const result = eval(history);
                        printOutput(result);
                        printHistory("");
                    } catch (err) {
                        printOutput("Error");
                        printHistory("");
                    }
                } else {
                    history += this.id;
                    printHistory(history);
                    printOutput("");
                }
            }
        }
    });
}

// Attach event listeners to number buttons
const numbers = document.getElementsByClassName("number");
for (let i = 0; i < numbers.length; i++) {
    numbers[i].addEventListener("click", function () {
        let output = reverseNumberFormat(getOutput());
        if (!isNaN(output)) {
            output = output.toString() + this.id;
            printOutput(output);
        }
    });
}
