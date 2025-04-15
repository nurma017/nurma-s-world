from telegram import Update
from telegram.ext import ContextTypes
import storage

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Привет! Я — бот для финансового планирования. Используй /help, чтобы узнать команды.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Команды:\n"
        "/config <категория> <лимит> — установить бюджет\n"
        "/log <категория> <сумма> — внести расход или доход\n"
        "/summary — показать баланс и бюджеты\n"
        "/notifyon — включить уведомления\n"
        "/notifyoff — выключить уведомления"
    )

async def config(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if len(args) != 2:
        await update.message.reply_text("❗ Пример: /config Food 50000")
        return

    category, limit = args[0], args[1]
    user_id = update.effective_user.id
    data = storage.load_data(user_id)

    if "budgets" not in data:
        data["budgets"] = {}
    data["budgets"][category] = int(limit)

    storage.save_data(user_id, data)
    await update.message.reply_text(f"✅ Бюджет на категорию '{category}' установлен: {limit} тг")

async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if len(args) != 2:
        await update.message.reply_text("❗ Пример: /log Food -1000 или /log Salary 30000")
        return

    category, amount = args[0], int(args[1])
    user_id = update.effective_user.id
    data = storage.load_data(user_id)

    if "records" not in data:
        data["records"] = []

    data["records"].append({"category": category, "amount": amount})
    storage.save_data(user_id, data)

    await update.message.reply_text(f"📥 Записано: {category} — {amount} тг")

async def summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    data = storage.load_data(user_id)

    total = 0
    categories = {}

    for record in data.get("records", []):
        total += record["amount"]
        cat = record["category"]
        categories[cat] = categories.get(cat, 0) + record["amount"]

    response = f"📊 Общий баланс: {total} тг\n\n"
    for cat, amt in categories.items():
        limit = data.get("budgets", {}).get(cat, None)
        if limit:
            response += f"{cat}: {amt} / {limit} тг\n"
        else:
            response += f"{cat}: {amt} тг (без лимита)\n"

    await update.message.reply_text(response)

async def notify_on(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔔 Уведомления включены (но пока не реализованы)")

async def notify_off(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔕 Уведомления выключены")