document.addEventListener('DOMContentLoaded', function() {
    const table = document.getElementById('data-table');
    const rows = table.getElementsByTagName('tr');

    for (let i = 1; i < rows.length; i++) {
        const cells = rows[i].getElementsByTagName('td');
        for (let j = 0; j < cells.length; j++) {
            const cellValue = cells[j].innerText;

            if (cellValue == "META") {                    
                cells[j].style.backgroundColor = 'pink';
            } else if (cellValue == "A TIER") {
                cells[j].style.backgroundColor = 'lightblue';
            } else if (cellValue == "B TIER") {
                cells[j].style.backgroundColor = 'blue';
            } else if (cellValue == "C TIER") {
                cells[j].style.backgroundColor = 'orange';
            } else {
                // cells[j].style.backgroundColor = 'grey';
            }
        }
    }
});