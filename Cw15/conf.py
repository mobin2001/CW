import psycopg2


DB_CONFIG = psycopg2.connect(
    dbname='student',
    user='postgres',
    password='123',
    host='37.32.5.219',
    port=5432
    )

conn = DB_CONFIG