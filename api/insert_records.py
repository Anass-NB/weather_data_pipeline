from api_request import mock_fetch_data
from api_request import fetch_data
import psycopg2


def connect_to_db():
    print("Connecting to Postgress Database ...")
    try:
        conn = psycopg2.connect(host="db",dbname="db",user="db_user",password="db_password",port=5432)
        return conn
    except Exception as e:
        print(f"Database COnnection failed : {e}")
        raise
            


def create_table(conn):
    print("Creating a table if not exist ...")
    try:
        cur = conn.cursor()
        cur.execute("""
                    CREATE SCHEMA IF NOT EXISTS dev;
                    CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                        id SERIAL PRIMARY KEY,
                        city TEXT,
                        temperature FLOAT,
                        weather_descriptions TEXT,
                        wind_speed FLOAT,
                        time TIMESTAMP,
                        inserted_at TIMESTAMP DEFAULT NOW(),
                        utc_offset TEXT
                    );
                    """)
        conn.commit()
        print("Table Created successfuly")
    except psycopg2.Error as e:
        print(f"Failed to create table {e}")
        raise

def insert_into_db(conn,data) : 
    print("Inserting data ...")
    try:
        cur = conn.cursor()
        cur.execute("""
                        INSERT INTO dev.raw_weather_data (
                            city ,
                            temperature ,
                            weather_descriptions ,
                            wind_speed ,
                            time ,
                            inserted_at ,
                            utc_offset 
                        ) values (%s,%s,%s,%s,%s,NOW(),%s);
                    """,(
                        data['location']['name'],
                        data['current']['temperature'],
                        data['current']['weather_descriptions'][0],
                        data['current']['wind_speed'],
                        data['location']['localtime'],
                        data['location']['utc_offset'], 
                    ))
        conn.commit()
        print("Data Inserted Successfully .. ")
    except psycopg2.Error as e:
        print(f"Failed to create table {e}")
        raise




def main():
    
    try:
        conn = connect_to_db()
        create_table(conn)
        data = fetch_data()
        insert_into_db(conn,data)
    except Exception as e : 
        print(f"An Error Accurs during execution function {e}")
    finally: 
        if 'conn' in locals():
            conn.close()
            print("Database COnnection closed .")
