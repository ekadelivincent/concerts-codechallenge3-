from band import Band
from venue import Venue

class Concert:
    def __init__(self, id, band_id, venue_id, date):
        self.id = id
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date

    @staticmethod
    def find_by_id(concert_id, conn):
        cur = conn.cursor()
        query = "SELECT * FROM concerts WHERE id = %s"
        cur.execute(query, (concert_id,))
        concert = cur.fetchone()
        cur.close()
        if concert:
            return Concert(concert[0], concert[1], concert[2], concert[3])
        return None

    def band(self, conn):
        return Band.find_by_id(self.band_id, conn)

    def venue(self, conn):
        return Venue.find_by_id(self.venue_id, conn)

    def hometown_show(self, conn):
        band = self.band(conn)
        venue = self.venue(conn)
        return band.hometown == venue.city

    def introduction(self, conn):
        band = self.band(conn)
        venue = self.venue(conn)
        return f"Hello {venue.city}!!!!! We are {band.name} and we're from {band.hometown}"
