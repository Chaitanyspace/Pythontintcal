function addCustomWindow() {
    // Access the elements by ID for custom windows
    const width = document.getElementById("width").value;
    const height = document.getElementById("height").value;
    const quantity = document.getElementById("quantity").value;
    const rate = document.getElementById("rate").value;
    const unit = document.getElementById("unit").value;

    // Check if any field is empty
    if (!width || !height || !quantity || !rate) {
        alert("Please fill in all fields.");
        return;
    }

    // Package data for the request
    const data = {
        width: width,
        height: height,
        quantity: quantity,
        rate: rate,
        unit: unit
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
    // Access the elements by ID for bulk orders
    const width = document.getElementById("bulkWidth").value;
    const height = document.getElementById("bulkHeight").value;
    const quantity = document.getElementById("bulkQuantity").value;
    const rate = document.getElementById("bulkRate").value;
    const unit = document.getElementById("unit").value;

    // Check if any field is empty
    if (!width || !height || !quantity || !rate) {
        alert("Please fill in all fields.");
        return;
    }

    // Package data for the request
    const data = {
        width: width,
        height: height,
        quantity: quantity,
        rate: rate,
        unit: unit
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
