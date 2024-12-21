import asyncio
from datetime import datetime
from bot.database import Database
import os

from config.settings import DATABASE_PATH
db = Database(DATABASE_PATH)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Absolute path to the `config` directory
DATABASE_PATH = os.path.join(BASE_DIR, "../reminders.db")  # Relative path to the database file


async def check_reminders(context):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    due_reminders = db.fetch_due_reminders(now)  # Ensure due reminders are fetched correctly
    print(f"Due reminders at {now}: {due_reminders}")  # Debugging
    for reminder in due_reminders:
        chat_id, reminder_text = reminder[1], reminder[2]
        await context.bot.send_message(chat_id=chat_id, text=f"⏰ Reminder: {reminder_text}")

