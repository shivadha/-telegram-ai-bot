import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from services.instagram_service import download_instagram_reel

TOKEN = os.environ.get("BOT_TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text

    if "instagram.com" in message:
        await update.message.reply_text("📥 Downloading Instagram reel...")

        success, response = download_instagram_reel(message)

        if success:
            await update.message.reply_text("✅ Reel downloaded successfully!")
        else:
            await update.message.reply_text(f"❌ Error: {response}")
    else:
        await update.message.reply_text("Send me an Instagram Reel link 🚀")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle_message))

app.run_polling()
