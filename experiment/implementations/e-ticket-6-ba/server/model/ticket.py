class Ticket:
    def __init__(self, artist, location, price, ticket_id = None):
        self.ticket_id = ticket_id
        self.artist = artist
        self. location = location
        self.price = price