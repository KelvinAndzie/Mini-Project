import hashlib
import mysql.connector
from flask import g

DATABASE = {
    "host": "localhost",
    "database": "career_guidance",
    "user": "root",
    "password": "riceBeans01",
}


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = Database()
    return db


class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=DATABASE["host"],
            database=DATABASE["database"],
            user=DATABASE["user"],
            password=DATABASE["password"],
        )
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), email VARCHAR(255), password VARCHAR(255))"
        )

    def insert(self, username, email, password):
        self.cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, self.hashpassword(password)),
        )
        self.conn.commit()

    def fetch(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        return self.cursor.fetchall()

    def login(self, username, password):
        self.cursor.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s",
            (username, self.hashpassword(password)),
        )
        return self.cursor.fetchall()

    def hashpassword(self, password):
        password = hashlib.sha256(password.encode()).hexdigest()
        return password

    def get_skills(self):
        self.cursor.execute("SELECT skill_name FROM skills")
        rows = self.cursor.fetchall()
        skills = [row[0] for row in rows]
        return skills

    def insert_recommended_roles(self, username, role, role_rank):
        # Check if the record already exists
        self.cursor.execute(
            """
            SELECT 1 FROM recommended_roles 
            WHERE user_id = (SELECT id FROM users WHERE username = %s) 
            AND role_id = (SELECT role_id FROM roles WHERE role = %s)
            """,
            (username, role),
        )
        existing_record = self.cursor.fetchone()

        if existing_record:
            # If the record exists, update it
            self.cursor.execute(
                """
                UPDATE recommended_roles 
                SET role_rank = %s
                WHERE user_id = (SELECT id FROM users WHERE username = %s) 
                AND role_id = (SELECT role_id FROM roles WHERE role = %s)
                """,
                (role_rank, username, role),
            )
        else:
            # If the record doesn't exist, insert a new one
            self.cursor.execute(
                """
                INSERT INTO recommended_roles (user_id, role_id, role_rank) 
                VALUES (
                    (SELECT id FROM users WHERE username = %s), 
                    (SELECT role_id FROM roles WHERE role = %s), 
                    %s
                )
                """,
                (username, role, role_rank),
            )

        self.conn.commit()

    def get_recommended_roles(self, username):
        self.cursor.execute(
            "SELECT r.role FROM recommended_roles rr INNER JOIN roles r ON rr.role_id = r.role_id WHERE rr.user_id=(SELECT users.id FROM users WHERE users.username=%s)",
            (username,),
        )
        rows = self.cursor.fetchall()
        recommended_roles = [row[0] for row in rows]
        # print(recommended_roles)
        return recommended_roles