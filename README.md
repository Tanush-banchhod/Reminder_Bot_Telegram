# Reminder Bot

A Telegram bot built using Python that allows users to set reminders and get notified when the reminder is due. The bot supports setting reminders for a specified duration and displays the active reminders.

## Features

- **Set Reminders**: Use the `/remind <seconds> <message>` command to set a reminder.
- **List Reminders**: Use the `/list` command to view all active reminders.
- **Automatic Notifications**: The bot sends reminders when they are due.
- **Database Integration**: Reminders are stored in an SQLite database for persistence.

## Requirements

- Python 3.x
- `python-telegram-bot` library
- SQLite (for database)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Tanush-banchhod/reminder-bot.git
   cd reminder-bot
   ```
2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up the bot token**:
   - Create a new bot using the BotFather on Telegram.
   - Copy the bot token and replace it in config/settings.py:
   ```python
      BOT_TOKEN = "YOUR_BOT_TOKEN"
   ```
5. **Run the bot**:
   ```python
   python main.py
   ```
   Your bot should now be running. You can interact with it via Telegram








