import sqlite3

class Database:
    """A simple database class to manage SQLite operations."""

    def __init__(self, db_name='myDB.db'):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.create_database()

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()

    def create_database(self):
        with self:
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS visitors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                visitor TEXT NOT NULL UNIQUE,
                date TEXT NOT NULL,
                comment TEXT NOT NULL
            )''')
            self.create_users_table()

    def create_users_table(self):
        with self:
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )''')
        with self:
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                comment TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )''')

        # Create table for users (if needed)
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )''')

        self.conn.commit()
        self.conn.close()

    def enter_comment(self, visitor, date, comment):
        with self:
            self.cursor.execute('''
            INSERT INTO visitors (visitor, date, comment) VALUES (?, ?, ?)
        ''', (visitor, date, comment))

    def get_comments(self):
        with self:
            self.cursor.execute('SELECT * FROM visitors')
            data = self.cursor.fetchall()
        return data

    def get_user(self, email):
        with self:
            self.cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
            user = self.cursor.fetchone()
        return user

    def add_user(self, email, password):
        with self:
            self.cursor.execute('''
            INSERT INTO users (email, password) VALUES (?, ?)
            ''', (email, password))

        self.conn.commit()


if __name__ == '__main__':
    with Database() as db:
        db.create_database()
        print("Database and tables created successfully.")