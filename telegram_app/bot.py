from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, MenuButtonWebApp, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8546749672:AAFuduIW1f1DFnQEFbk0TQtyASWFyCWaG7c"
WEB_APP_URL = "https://www.youtube.com/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Set the menu button (Open App button at the bottom)
    await context.bot.set_chat_menu_button(
        chat_id=update.effective_chat.id,
        menu_button=MenuButtonWebApp(
            text="Open App",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )
    )
    
    welcome_text = (
        "👋 Welcome to Coffee Shop Bot!\n"
        "☕ Click below to open our menu or visit other pages."
    )

    await update.message.reply_photo(
        photo="https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&fit=crop&w=800&q=80",
        caption=welcome_text
    )

    keyboard = [
        [InlineKeyboardButton("☕ Open Coffee Menu", url=WEB_APP_URL)],
        [InlineKeyboardButton("ℹ️ About Us", url=f"{WEB_APP_URL}/about")],
        [InlineKeyboardButton("📞 Contact", url=f"{WEB_APP_URL}/contact")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Choose an option below:", reply_markup=reply_markup)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Coffee Shop Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()