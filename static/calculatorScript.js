document.addEventListener('DOMContentLoaded', function() {
    var calculatorButtons = document.querySelectorAll(".btn-calculator");
    var result = document.querySelector("#calculator-result")
    calculatorButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            if (event.target.id === "calc-button-c") {
                result.value = "";
            } else if (event.target.id === "calc-button-=") {
                result.value = math.eval(result.value)
            } else {
                result.value += event.target.value
            };
        });
    });
 });