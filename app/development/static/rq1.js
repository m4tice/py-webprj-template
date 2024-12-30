document.addEventListener("DOMContentLoaded", function() {
    const table = document.getElementById("data-table");
    const states = table.getElementsByClassName("state"); 
    const doors = table.getElementsByClassName("DOORS");
    
    // LCS check
    for (let i = 0; i < states.length; i++){
        const stateCell = states[i];

        if ("Conflicted" === stateCell.innerText) {
            stateCell.style.backgroundColor = "#FFC000";
            stateCell.style.fontWeight = "bold";
        }

        else if ("Evaluated" === stateCell.innerText) {
            stateCell.style.backgroundColor = "#FFE699";
            stateCell.style.fontWeight = "bold";
        }
    }

    // DOORS check
    for (let i = 0; i < doors.length; i++){
        const doorCell = doors[i];

        if ("missing" === doorCell.innerText) {
            doorCell.style.backgroundColor = "#FF7C80";
            doorCell.style.color = "white";
            doorCell.style.fontWeight = "bold";
        }
    }
});