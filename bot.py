# -------------------------
# NORMAL VERSION BOT (PTB v20)
# -------------------------
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# ==== SETTINGS ====

BOT_TOKEN = os.getenv("8299033526:AAH38ZmbJASl_aXTlsD2Whvem86pcxnV9nA")

CHANNELS = [
    -1003363555359,    # Channel 1 ID
    -1003363555359,    # Channel 2 ID
    -1003406630615     # Backup Channel ID
]

VIDEO_CHAT_ID = -1003366304782
VIDEO_MESSAGE_ID = 2

# ========== START COMMAND ==========
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("JOIN CHANNEL 1", url="https://t.me/vvsvdios")],
        [InlineKeyboardButton("JOIN CHANNEL 2", url="https://t.me/+lPLEtH00nbVlNzM1")],
        [InlineKeyboardButton("JOIN BACKUP CHANNEL", url="https://t.me/+otMttzfN6nthZTc1")],
        [InlineKeyboardButton("Joined ✅", callback_data="check_join")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🔥 Welcome to Viral Videos Bot 🔥\n\n"
        "👉 Aage badhne ke liye niche diye gaye 3 channels ko join karein:\n\n"
        "1️⃣ Channel 1\n"
        "2️⃣ Channel 2\n"
        "3️⃣ Backup Channel\n\n"
        "✔️ Sab join karne ke baad 'Joined ✅' dabayein.",
        reply_markup=reply_markup
    )

# ========== CHECK JOIN ==========
async def check_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    not_joined = []

    for channel in CHANNELS:
        try:
            member = await context.bot.get_chat_member(channel, user_id)
            if member.status in ["left", "kicked"]:
                not_joined.append(channel)
        except Exception:
            not_joined.append(channel)

    if not_joined:
        await query.message.reply_text("❌ Please join all 3 channels to get the video.")
        return

    # Send video
    await context.bot.copy_message(
        chat_id=query.from_user.id,
        from_chat_id=VIDEO_CHAT_ID,
        message_id=VIDEO_MESSAGE_ID
    )

# ========== RUN BOT ==========
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(check_join))

    print("Bot is running...")
    app.run_polling()

main()


