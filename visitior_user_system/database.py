import sqlite3


def create_database():
    conn = sqlite3.connect('myDB.db')
    cursor = conn.cursor()
    
    # Create table for visitors
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS visitors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        visitor TEXT NOT NULL UNIQUE,
        date TEXT NOT NULL,
        comment TEXT NOT NULL
    )''')

    # Create table for users (if needed)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )''')

    conn.commit()
    conn.close()


def enter_comment(visitor, date, comment):
    conn = sqlite3.connect('myDB.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO visitors (visitor, date, comment) VALUES (?, ?, ?)
    ''', (visitor, date, comment))
    
    conn.commit()    
    cursor.close()
    conn.close()

def get_comments():
    conn = sqlite3.connect('myDB.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM visitors')
    data = cursor.fetchall()
    
    conn.close()
    return data


def get_user(email):
    conn = sqlite3.connect('myDB.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()
    
    conn.close()
    return user

def add_user(email, password):
    conn = sqlite3.connect('myDB.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO users (email, password) VALUES (?, ?)
    ''', (email, password))
    
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    create_database()
    print("Database and tables created successfully.")