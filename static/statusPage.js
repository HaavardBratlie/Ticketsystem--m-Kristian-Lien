async function getTickets(){
    try{
        const response = await fetch("/api/tickets")

        const data = await response.json()
    
        if(data.status = "success"){
            console.log(data)
            populateTable(data)
        }
        else{
            console.log(data.message)
        }
    }
    catch(error){
        console.log(error)
    }
}

function populateTable(tickets){
    const tableBodyEl = document.getElementById("status-table-body")

    tickets.forEach(ticket => {
        const {name, email, message, status, ticket_id } = ticket;
        const tableRow = document.createElement("tr");

        tableRow.innerHTML = `
            <td>${inquiry}</td>
            <td>${name}</td>
            <td>${email}</td>
            <td>${message}</td>
            <td>${status}</td>
            <td>${ticket_id}</td>
        `;
    
        tableBodyEl.appendChild(tableRow)
    });
}

getTickets()