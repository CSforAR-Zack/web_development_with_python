import sqlite3


def create_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
  # Create table for users
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS visitors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        visitor TEXT NOT NULL UNIQUE,
        date TEXT NOT NULL,
        reason TEXT NOT NULL
    )''')
    
    conn.commit()
    conn.close()


def enter_data(visitor, date, reason):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO visitors (visitor, date, reason) VALUES (?, ?, ?)
    ''', (visitor, date, reason))
    
    conn.commit()
    conn.close()

def get_visitors():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM visitors')
    data = cursor.fetchall()
    
    conn.close()
    return data


if __name__ == '__main__':
    create_database()
    print("Database and tables created successfully.")