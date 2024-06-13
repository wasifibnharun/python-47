import sqlite3

class Database:
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY, student_name text,student_class text, student_roll INTEGER, student_section text, guardian_contact text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute('SELECT * FROM students')
        rows=self.cur.fetchall()
        return rows
    
    def insert(self,student_name,student_class,student_roll,student_section,guardian_contact):
        self.cur.execute("INSERT INTO students VALUES(NULL,?,?,?,?,?)",(student_name,student_class,student_roll,student_section,guardian_contact))
        self.conn.commit()

    def delete(self,id):
        self.cur.execute("DELETE FROM students WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,student_name,student_class,student_roll,student_section,guardian_contact):
        self.cur.execute("UPDATE students SET student_name=?,student_class=?,student_roll=?,student_section=?,guardian_contact=? WHERE id=?",(student_name,student_class,student_roll,student_section,guardian_contact,id))
        self.conn.commit()
