import os
import sqlite3
from model.ticket import Ticket

class SqlDataService:
    def __init__(self):
        # Setting database path dynamically
        base_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(base_dir, '..', '..'))
        self.path = os.path.join(project_root, 'database.db')

        # Ticket Constants
        self.table_tickets = 'tickets'
        self.field_tickets_id = 'id'
        self.field_tickets_artist = 'artist'
        self.field_tickets_location = 'location'
        self.field_tickets_price = 'price'

    def execute_query(self, query, values = None):
        conn = None
        try:
            conn = sqlite3.connect(self.path)
            cursor = conn.cursor()

            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)

            if cursor.description is not None:
                results = cursor.fetchall()
                return results
            else:
                conn.commit()
                return 0

        except sqlite3.Error as e:
            print("SQLite error:", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    # Ticket Functions
    def retrieve_tickets(self):
        query = f'SELECT * FROM {self.table_tickets} ORDER BY {self.field_tickets_id} DESC'
        print(query)

        entries = self.execute_query(query)
        results = [Ticket(e[1], e[2], e[3], e[0]) for e in entries]
        return results

    def insert_ticket(self, new_ticket):
        query = f'INSERT INTO {self.table_tickets} ({self.field_tickets_artist}, {self.field_tickets_location}, {self.field_tickets_price}) VALUES (?, ?, ?)'
        values = (new_ticket.artist, new_ticket.location, new_ticket.price)
        print(query)

        result = self.execute_query(query, values)
        return result

    def delete_ticket(self, ticket_id: int) -> bool:
        """
        Delete the ticket row with the given ID; return True if exactly one row was deleted.
        """
        # Build a parameterized DELETE statement using your table and ID field names
        query = f"DELETE FROM {self.table_tickets} WHERE {self.field_tickets_id} = ?"
        values = (ticket_id,)

        print(f"[SQL] {query}  values={values}")

        # execute_query should run the DELETE and return the number of affected rows
        rows_affected = self.execute_query(query, values)

        # Depending on your implementation, execute_query might return None or 
        # some cursor/result – adjust if necessary. If it returns cursor, you can do:
        # rows_affected = cursor.rowcount

        return rows_affected == 1
