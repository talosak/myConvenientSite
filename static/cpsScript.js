document.addEventListener('DOMContentLoaded', function() {
    var cpsButton = document.querySelector("#cps-button")
    var clickCounterDisplay = document.querySelector("#cps-clicks")
    var timeRemainingDisplay = document.querySelector("#cps-time-remaining")
    var isStarted = 0;
    var timeRemaining = 10;
    var clickCounter = 0;

    cpsButton.addEventListener('click', (event) => {
         if (isStarted == 0) {
             startTimer();
         }
         clickCounter += 1;
         clickCounterDisplay.innerHTML = "Clicks: " + clickCounter;
    })

    function startTimer() {
         isStarted = 1;
         var timer = setInterval(function() {
             timeRemaining -= 1;
             timeRemainingDisplay.innerHTML = "Time remaining: " + timeRemaining;
             if (timeRemaining <= 0) {
                clearInterval(timer);
                endTimer();
            }
        }, 1000)
    }

    function endTimer() {
         document.querySelector("#cps-hidden-id").value = clickCounter;
         document.querySelector("#cps-form").submit();
    }
})