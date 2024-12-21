from datetime import datetime, timedelta
from telegram import Update
from telegram.ext import ContextTypes
from bot.database import Database
import asyncio
import os

from config.settings import DATABASE_PATH
db = Database(DATABASE_PATH)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Absolute path to the `config` directory
DATABASE_PATH = os.path.join(BASE_DIR, "../reminders.db")  # Relative path to the database file


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Use /remind to set reminders.")

async def set_reminder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if len(args) < 2:
        await update.message.reply_text("Usage: /remind <seconds> <message>")
        return

    delay = int(args[0])
    reminder_text = " ".join(args[1:])
    remind_at = datetime.now() + timedelta(seconds=delay)

    db.add_reminder(update.message.chat_id, reminder_text, remind_at)
    await update.message.reply_text(f"Reminder set for {delay} seconds.")

async def set_reminder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if len(args) < 2:
        await update.message.reply_text("Usage: /remind <seconds> <message>")
        return

    delay = int(args[0])
    reminder_text = " ".join(args[1:])
    remind_at = datetime.now() + timedelta(seconds=delay)

    db.add_reminder(update.message.chat_id, reminder_text, remind_at)
    
    # Debugging statement
    print(f"Reminder added: Chat ID {update.message.chat_id}, Reminder '{reminder_text}', Time {remind_at}")
    
    await update.message.reply_text(f"Reminder set for {delay} seconds.")

async def list_reminders(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    reminders = db.fetch_user_reminders(chat_id)  # Ensure you're using the correct method
    
    # Debugging statement
    print(f"Fetching reminders for Chat ID {chat_id}")
    
    if not reminders:
        await update.message.reply_text("No active reminders.")
        return

    response = "\n".join([f"{r[0]}. {r[1]} at {r[2]}" for r in reminders])
    await update.message.reply_text(f"Your reminders:\n{response}")





