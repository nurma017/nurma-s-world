from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from handlers import start, help_command, config, log, summary, notify_on, notify_off
from config import TOKEN
from telegram.request import HTTPXRequest

request = HTTPXRequest(connect_timeout=10.0, read_timeout=10.0)

app = Application.builder().token(TOKEN).request(request).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("config", config))
app.add_handler(CommandHandler("log", log))
app.add_handler(CommandHandler("summary", summary))
app.add_handler(CommandHandler("notifyon", notify_on))
app.add_handler(CommandHandler("notifyoff", notify_off))

if __name__ == '__main__':
    app.run_polling()
