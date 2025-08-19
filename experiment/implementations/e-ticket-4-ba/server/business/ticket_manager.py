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
    def delete_ticket(ticket_id: int) -> bool:
        """
        Delete a ticket by its ID.
        Returns True if a row was deleted, False otherwise.
        """
        # Delegate deletion to the data layer
        data_service = SqlDataService()
        # Perform delete; SqlDataService.delete_ticket should return a boolean
        return data_service.delete_ticket(ticket_id)
