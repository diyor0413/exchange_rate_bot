import sqlite3 as sq

class DataBase:

    def __init__(self, db_files):
        self.connect = sq.connect(db_files)
        self.cursor = self.connect.cursor()

    async def add_users(self, user_id, name):
        with self.connect: #используем with чтобы не писать connect.cloce
            return self.cursor.execute("""INSERT INTO users(user_id, name) VALUES (?,?)""",
                                       [user_id, name])
