import psycopg2

# Database connection function
def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname="ekadeli",
            user="ekadeli",
            password="ekadeli",
            host="localhost"
        )
        return conn
    except Exception as error:
        print(f"Error connecting to the database: {error}")
        return None

# Testing the classes
from band import Band
from venue import Venue
from concert import Concert

if __name__ == "__main__":
    conn = get_db_connection()

    # Test creating a band and retrieving data
    band = Band.find_by_id(1, conn)
    if band:
        print(f"Band: {band.name}, Hometown: {band.hometown}")
        print("Concerts:", band.concerts(conn))
        print("Venues:", band.venues(conn))

    # Test creating a venue and retrieving data
    venue = Venue.find_by_id(1, conn)
    if venue:
        print(f"Venue: {venue.title}, City: {venue.city}")
        print("Concerts:", venue.concerts(conn))
        print("Bands:", venue.bands(conn))

    # Test creating a concert and retrieving data
    concert = Concert.find_by_id(1, conn)
    if concert:
        print(f"Concert on {concert.date}")
        print(f"Band: {concert.band(conn).name}")
        print(f"Venue: {concert.venue(conn).title}")
        print(f"Hometown Show: {concert.hometown_show(conn)}")
        print(f"Introduction: {concert.introduction(conn)}")

    if conn:
        conn.close()  # Close connection when done
