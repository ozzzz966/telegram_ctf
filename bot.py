from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "7617303557:AAGR3AnLQZjjerpcp279nLq5JQKg3ft5naY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if args:
        print(f"Payload: {args[0]} від {update.effective_user.username}")

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Відкрити WebApp", web_app={"url": "https://yourname.github.io/telegram-ctf/webapp.html"})]
    ])

    await update.message.reply_text("Натисни кнопку нижче для продовження:", reply_markup=keyboard)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
