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
        const resp = await fetch('http://127.0.0.1:5000/delete_ticket', {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id })
        });
        if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
        const data = await resp.json();
        console.log('deleteTicket result:', data);
        return data;
    } catch (err) {
        console.error('Error in deleteTicket():', err);
        alert('Failed to delete ticket. See console.');
    }
}

function handleReset() {
    document.getElementById('ticket-insert-form').reset();
}

/**
 * Reads the inputs, calls addTicket(), then resets form
 * and refreshes the tickets list.
 */
async function handleSubmit() {
    // Grab values
    const artist = document.getElementById('artist-input').value;
    const location = document.getElementById('location-input').value;
    const price = parseInt(document.getElementById('price-input').value, 10);

    // Post to the server
    await addTicket(artist, location, price);

    // Clear the form
    handleReset();

    // Refresh your view (if you're on the tickets page)
    await updateTicketsTable();

    // Optionally navigate back to the list view:
    pageNumber = 0;
    saveSessionData();
    updatePage();
}