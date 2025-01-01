document.addEventListener("DOMContentLoaded", function() {
    const table = document.getElementById("rq1-table");
    const states = table.getElementsByClassName("state"); 
    const doors = table.getElementsByClassName("DOORS");
    const rows = table.getElementsByTagName("tr");

    for (let i = 1; i < rows.length; i++){
        const row = rows[i];

        // State of element
        const lifeCycleState = row.getElementsByTagName("td")[2];
        
        // allocation
        const allocation = row.getElementsByTagName("td")[8];

        // category
        const category = row.getElementsByTagName("td")[9];

        // DOORS
        const doors = row.getElementsByTagName("td")[10];

        // Life Cycle State validation
        if ("Conflicted" === lifeCycleState.innerText) {
            lifeCycleState.style.backgroundColor = "#FFC000";
            lifeCycleState.style.fontWeight = "bold";
        }

        else if ("Evaluated" === lifeCycleState.innerText) {
            lifeCycleState.style.backgroundColor = "#FFE699";
            lifeCycleState.style.fontWeight = "bold";
        }

        // Allocation, Category and DOORS validation
        if ("None" === allocation.innerText) {
            allocation.style.backgroundColor = "#FFC000";
            allocation.style.fontWeight = "bold";
        }

        if (("Software" === allocation.innerText) && ("None" === doors.innerText)) {
            doors.style.backgroundColor = "#FF7C80";
            doors.style.color = "white";
            doors.style.fontWeight = "bold";
        }
    }
});