from telegram.ext import Application, CommandHandler
from config.settings import BOT_TOKEN
from bot.handlers import start, set_reminder, list_reminders
from bot.scheduler import check_reminders

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("remind", set_reminder))
    application.add_handler(CommandHandler("list", list_reminders))

    application.job_queue.run_repeating(check_reminders, interval=60, first=0)

    print("Bot is running... Press Ctrl+C to stop.")
    application.run_polling()

if __name__ == "__main__":
    main()
