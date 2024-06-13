import sqlite3

class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS articles (id INTEGER AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(100), body TEXT, create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM articles")
        articles = self.cur.fetchall()
        return articles

    def insert(self,title,author,body,create_date):
        self.cur.execute("INSERT INTO articles VALUES (NULL,?,?,?,?)",(title,author,body,create_date))
        self.conn.commit()