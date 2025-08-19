async function getTickets() {
    try {
        const response = await fetch(`http://127.0.0.1:5000/get_tickets`);

        if (!response.ok) {
            throw new Error('error');
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error with GET request:', error);
    }
}

function addTicket(artist, location, price) {
    return fetch('http://127.0.0.1:5000/add_ticket', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 'artist': artist, 'location': location, 'price': price })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

async function deleteTicket(id) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/delete_ticket/${id}`, {
            method: 'DELETE'
        });

        if (response.status === 404) {
            throw new Error('Ticket not found');
        }
        if (!response.ok) {
            throw new Error('Server error on delete');
        }

        // Optionally read a JSON body if your server returns one:
        // const data = await response.json();
        // console.log('Delete response:', data);

    } catch (error) {
        console.error('Error with DELETE request:', error);
        throw error;  // so calling code knows it failed
    }
}
