import sqlite3

con = sqlite3.connect("library.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTIGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50) NOT NULL,
            surname VARCHAR(50) NOT NULL,
            email VARCHAR(50) NOT NULL UNIQUE,
            phone VARCHAR(12) NOT NULL)""")

cur.execute("""CREATE TABLE IF NOT EXISTS transactions
            (
            id INTIGER PRIMARY KEY AUTOINCREMENT,
            amount DECIMAL(10,2) NOT NULL,
            userfrom_id INTIGER NOT NULL.
            userto_id INTIGER NOT NULL,
            date VARCHAR(20) NOT NULL,
            FORGERY KEY (userfrim_id) REFERENCES users
            )
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS credentials
               (
                   id       INTEGER PRIMARY KEY AUTOINCREMENT,
                   login    VARCHAR(50)  NOT NULL,
                   password VARCHAR(150) NOT NULL,
                   user_id  INTEGER      NOT NULL,
                   FOREIGN KEY (user_id) REFERENCES users (id)
               )
            """)