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
            createData(data[buttonId]);
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