import psycopg2

# Open a connection to the database
conn = psycopg2.connect(
    host="localhost",
    database="flask_database",
    user="postgres",
    password="123456789Aa@")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS books;')
cur.execute('DROP TABLE IF EXISTS accounts;')

cur.execute('CREATE TABLE accounts (id serial PRIMARY KEY,'
            'username varchar (15) NOT NULL,'
            'password varchar(20) NOT NULL);'
            )

cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
            'title varchar (150) NOT NULL,'
            'author varchar (50) NOT NULL,'
            'pages_num integer NOT NULL,'
            'review text,'
            'date_added date DEFAULT CURRENT_TIMESTAMP);'
            )

# Insert data into the table
cur.execute('INSERT INTO accounts (username, password)'
            'VALUES (%s, %s)',
            ('phibien',
             '123456789')
            )

cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('A Tale of Two Cities',
             'Charles Dickens',
             489,
             'A great classic!')
            )

cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Anna Karenina',
             'Leo Tolstoy',
             864,
             'Another great classic!')
            )

conn.commit()

cur.close()
conn.close()
