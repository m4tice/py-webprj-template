document.addEventListener('DOMContentLoaded', function() {
    fetchData();
});

function fetchData() {
    fetch('/table-js/data')
        .then(response => response.json())
        .then(data => {
            for (let i = 0; i < data.length; i++) {
                createButton(i);
            }
        });
}

function createButton(buttonId) {
    const button = document.createElement('button');
    button.innerHTML = buttonId;
    button.className = 'btn btn-primary';
    button.onclick = function() {
        fetch('/table-js/data')
        .then(response => response.json())
        .then(data => {
            createTable(data[buttonId]);
        });
    }
    document.body.appendChild(button);
}

function createData(data) {
    const existingParagraph = document.querySelector('p');
    if (existingParagraph) {
        existingParagraph.remove();
    }

    const paragraph = document.createElement('p');
    paragraph.textContent = JSON.stringify(data);
    document.body.appendChild(paragraph);
}

function createTable(data) {
    const existingTable = document.querySelector('table');
    if (existingTable) {
        existingTable.remove();
    }

    const tableHeaders = ['Name', 'Occupation', 'Age'];
    
    const table = document.createElement('table');
    table.className = 'table table-striped';

    const thead = document.createElement('thead');
    const headerRow = document.createElement('tr');
    tableHeaders.forEach(headerText => {
        const header = document.createElement('th');
        header.className = 'table-dark';
        header.textContent = headerText;
        headerRow.appendChild(header);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);

    const tbody = document.createElement('tbody');
    const row = document.createElement('tr');
    data.forEach(item => {
        const cell = document.createElement('td');
        cell.textContent = item;
        row.appendChild(cell);
    });
    tbody.appendChild(row);
    table.appendChild(tbody);

    document.body.appendChild(table);
}