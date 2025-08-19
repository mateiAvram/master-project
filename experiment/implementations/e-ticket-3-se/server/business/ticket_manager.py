from model.ticket import Ticket
from data.sql_data_service import SqlDataService

class TicketManager:

    @staticmethod
    def retrieve_tickets():
        data_service = SqlDataService()
        tickets = data_service.retrieve_tickets()
        return [{'id': t.ticket_id, 'artist': t.artist, 'location': t.location, 'price': t.price} for t in tickets]

    @staticmethod
    def insert_ticket(data):
        artist = data.get('artist')
        location = data.get('location')
        price = data.get('price')
        
        data_service = SqlDataService()
        return data_service.insert_ticket(Ticket(artist, location, price))

    @staticmethod
    def delete_ticket(data):
        """
        data: dict containing {'id': <ticket_id>}
        Returns True on success, False or raises on failure.
        """
        ticket_id = data.get('id')
        if ticket_id is None:
            raise ValueError("Missing 'id' in delete_ticket payload")
        ds = SqlDataService()
        return ds.delete_ticket(ticket_id)

