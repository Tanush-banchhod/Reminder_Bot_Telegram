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
   git clone https://github.com/yourusername/reminder-bot.git
   cd reminder-bot
