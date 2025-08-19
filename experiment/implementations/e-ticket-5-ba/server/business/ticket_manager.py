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
        # 1. Pull the ticket ID out of the JSON payload
        ticket_id = data.get('id')
        if ticket_id is None:
            raise KeyError("Missing 'id' in delete request")

        # 2. Call your data layer to delete
        data_service = SqlDataService()
        deleted_rows = data_service.delete_ticket(ticket_id)

        # 3. If nothing was deleted, raise so the API can return 404
        if deleted_rows == 0:
            raise Exception(f"Ticket {ticket_id} not found")

        # 4. Otherwise, return success (you can return deleted_rows if you like)
        return deleted_rows

