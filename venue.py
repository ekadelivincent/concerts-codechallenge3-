class Venue:
    def __init__(self, id, title, city):
        self.id = id
        self.title = title
        self.city = city

    @staticmethod
    def find_by_id(venue_id, conn):
        cur = conn.cursor()
        query = "SELECT * FROM venues WHERE id = %s"
        cur.execute(query, (venue_id,))
        venue = cur.fetchone()
        cur.close()
        if venue:
            return Venue(venue[0], venue[1], venue[2])
        return None

    def concerts(self, conn):
        cur = conn.cursor()
        query = "SELECT * FROM concerts WHERE venue_id = %s"
        cur.execute(query, (self.id,))
        concerts = cur.fetchall()
        cur.close()
        return concerts

    def bands(self, conn):
        cur = conn.cursor()
        query = """
        SELECT bands.* FROM bands
        JOIN concerts ON concerts.band_id = bands.id
        WHERE concerts.venue_id = %s
        """
        cur.execute(query, (self.id,))
        bands = cur.fetchall()
        cur.close()
        return bands

    def concert_on(self, date, conn):
        cur = conn.cursor()
        query = "SELECT * FROM concerts WHERE venue_id = %s AND date = %s"
        cur.execute(query, (self.id, date))
        concert = cur.fetchone()
        cur.close()
        return concert

    def most_frequent_band(self, conn):
        cur = conn.cursor()
        query = """
        SELECT bands.*, COUNT(concerts.id) AS num_concerts 
        FROM bands 
        JOIN concerts ON concerts.band_id = bands.id
        WHERE concerts.venue_id = %s
        GROUP BY bands.id
        ORDER BY num_concerts DESC
        LIMIT 1
        """
        cur.execute(query, (self.id,))
        band = cur.fetchone()
        cur.close()
        return band
