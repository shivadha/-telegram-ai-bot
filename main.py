from services.instagram_service import fetch_instagram_metadata

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text

    if "instagram.com" in message:
        await update.message.reply_text("🔍 Fetching reel metadata...")

        success, data = fetch_instagram_metadata(message)

        if success:
            title = data.get("title", "No title")
            author = data.get("author_name", "Unknown")

            await update.message.reply_text(
                f"📌 Title: {title}\n👤 Author: {author}\n\nNow send 2-4 images of Shivit."
            )
        else:
            await update.message.reply_text(f"❌ Error: {data}")
    else:
        await update.message.reply_text("Send me an Instagram Reel link 🚀")
