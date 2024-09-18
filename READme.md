# Concert Management System

This project is a simple Python application to manage concerts, bands, and venues using raw SQL queries with `psycopg2`. The application interacts with a PostgreSQL database containing three tables: `bands`, `venues`, and `concerts`.

## Database Schema

### Tables

- **Bands Table**
  - `name`: String - the name of the band
  - `hometown`: String - the hometown of the band

- **Venues Table**
  - `title`: String - the title of the venue
  - `city`: String - the city where the venue is located

- **Concerts Table**
  - `id`: Integer - unique identifier for each concert
  - `band_name`: String - name of the band performing
  - `venue_title`: String - title of the venue where the concert is held
  - `date`: String - date of the concert (in `YYYY-MM-DD` format)

## Requirements

- Python 3.x
- PostgreSQL
- `psycopg2` library

### Python Libraries

To install the required `psycopg2` library, run the following command:

```bash
pip install psycopg2
