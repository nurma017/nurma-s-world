from telegram import Update
from telegram.ext import ContextTypes
import storage

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to your Financial Planner Bot! Use /help to get commands.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""📌 Available commands:
/config — Set budget (e.g. /config Food 50000)
/log — Log expense or income (e.g. /log Food -1000)
/summary — Show current balance
/notifyon — Enable notifications
/notifyoff — Disable notifications""")

async def config(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💰 Budget set (example: /config Food 50000)")

async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Logged expense/income (example: /log Food -1000)")

async def summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Balance: 24000 KZT\nFood: 12000/50000")

async def notify_on(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔔 Notifications ON")

async def notify_off(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔕 Notifications OFF")