function addCustomWindow() {
    const data = {
        width: document.getElementById("width").value,
        height: document.getElementById("height").value,
        quantity: document.getElementById("quantity").value,
        rate: document.getElementById("rate").value,
        unit: document.getElementById("unit").value
    };

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams(data)
    })
    .then(response => response.json())
    .then(result => addToTable(result))
    .catch(error => console.error('Error:', error));
}

function addBulkOrder() {
    const data = {
        width: document.getElementById("bulkWidth").value,
        height: document.getElementById("bulkHeight").value,
        quantity: document.getElementById("bulkQuantity").value,
        rate: document.getElementById("bulkRate").value,
        unit: document.getElementById("unit").value
    };

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams(data)
    })
    .then(response => response.json())
    .then(result => addToTable(result))
    .catch(error => console.error('Error:', error));
}

function addToTable(result) {
    const tableBody = document.getElementById("tableBody");
    const row = document.createElement("tr");
    row.innerHTML = `
        <td>${result.date}</td>
        <td>${result.time}</td>
        <td>${result.width}</td>
        <td>${result.height}</td>
        <td>${result.quantity}</td>
        <td>${result.area_sqm}</td>
        <td>${result.cost}</td>
    `;
    tableBody.appendChild(row);
}
