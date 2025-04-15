from telegram.ext import Application, CommandHandler
from handlers import start  
from config import TOKEN

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))


app.run_polling()