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

/**
 * Sends a DELETE request to remove the ticket with the given id.
 * @param {number|string} id
 * @returns {Promise<object>} the JSON response { success: true } or { success: false, error }
 */
async function deleteTicket(id) {
    const res = await fetch(`/api/tickets/${id}`, {
        method: 'DELETE'
    });
    return res.json();
}

