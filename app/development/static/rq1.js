document.addEventListener("DOMContentLoaded", function() {
    const table = document.getElementById("data-table");
    const rows = table.getElementsByClassName("state"); 
    
    for (let i = 0; i < rows.length; i++){
        if ("Conflicted" === rows[i].innerText) {
            rows[i].style.backgroundColor = "#FF9AA2";
            rows[i].style.color = "#FFFFFF";
            rows[i].style.fontWeight = "bold";
        }
    }
});