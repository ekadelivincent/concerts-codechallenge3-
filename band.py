class Band:
    def __init__(self, id, name, hometown):
        self.id = id
        self.name = name
        self.hometown = hometown

    @staticmethod
    def find_by_id(band_id, conn):
        cur = conn.cursor()
        query = "SELECT * FROM bands WHERE id = %s"
        cur.execute(query, (band_id,))
        band = cur.fetchone()
        cur.close()
        if band:
            return Band(band[0], band[1], band[2])
        return None

    def concerts(self, conn):
        cur = conn.cursor()
        query = "SELECT * FROM concerts WHERE band_id = %s"
        cur.execute(query, (self.id,))
        concerts = cur.fetchall()
        cur.close()
        return concerts

    def venues(self, conn):
        cur = conn.cursor()
        query = """
        SELECT venues.* FROM venues
        JOIN concerts ON concerts.venue_id = venues.id
        WHERE concerts.band_id = %s
        """
        cur.execute(query, (self.id,))
        venues = cur.fetchall()
        cur.close()
        return venues

    def play_in_venue(self, venue_id, date, conn):
        cur = conn.cursor()
        query = "INSERT INTO concerts (band_id, venue_id, date) VALUES (%s, %s, %s)"
        cur.execute(query, (self.id, venue_id, date))
        conn.commit()
        cur.close()

    @staticmethod
    def most_performances(conn):
        cur = conn.cursor()
        query = """
        SELECT bands.*, COUNT(concerts.id) AS num_concerts 
        FROM bands 
        JOIN concerts ON concerts.band_id = bands.id
        GROUP BY bands.id
        ORDER BY num_concerts DESC
        LIMIT 1
        """
        cur.execute(query)
        band = cur.fetchone()
        cur.close()
        if band:
            return Band(band[0], band[1], band[2])
        return None
