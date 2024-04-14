import mysql.connector
from config import USER, PASSWORD, HOST

class DbConnectionError(Exception):
    pass


def connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx

def _map_values(availability):
    mapped = []
    for item in availability:
        mapped.append({
            'artist': item[0],
            'tour_date': item[1],
            'tickets_available': item[2]
        })
    return mapped


def get_tour_dates(_date):
    tour_dates = []
    try:
        db_name = 'concerts'
        db_connection = connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to database: {db_name}")

        query = """
        SELECT artist, tour_date, tickets_available
        FROM tour_dates
        WHERE tour_date = '{}'
        """.format(_date)

        cur.execute(query)

        result = cur.fetchall()
        tour_dates = _map_values(result)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to connect to database")

    finally:
        if db_connection:
            db_connection.close()
            print("Connection closed")

    return tour_dates
