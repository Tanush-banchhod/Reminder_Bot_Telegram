import sqlite3

class Database:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS reminders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id INTEGER NOT NULL,
            reminder_text TEXT NOT NULL,
            remind_at DATETIME NOT NULL
        )
        """)
        self.conn.commit()

    def add_reminder(self, chat_id, reminder_text, remind_at):
        self.cursor.execute("INSERT INTO reminders (chat_id, reminder_text, remind_at) VALUES (?, ?, ?)",
                            (chat_id, reminder_text, remind_at))
        self.conn.commit()

    def fetch_due_reminders(self, now):
        self.cursor.execute("SELECT id, chat_id, reminder_text FROM reminders WHERE remind_at <= ?", (now,))
        reminders = self.cursor.fetchall()
        self.cursor.execute("DELETE FROM reminders WHERE remind_at <= ?", (now,))
        self.conn.commit()
        return reminders

    def fetch_user_reminders(self, chat_id):
        self.cursor.execute("SELECT id, reminder_text, remind_at FROM reminders WHERE chat_id = ?", (chat_id,))
        reminders = self.cursor.fetchall()
        print(f"Reminders fetched for {chat_id}: {reminders}")  # Debugging
        return reminders
