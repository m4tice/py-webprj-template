function button3_clicked(count) {
    fetch(`/get-request/clicked/${count}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById("count").innerHTML = data.data;
        })
}

function get_current_count(){
    return Number(document.getElementById("count").innerHTML);
}