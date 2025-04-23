from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Bot tokenini kiriting
TOKEN = 'SIZNING_BOT_TOKEN'


# /start komandasi uchun funksiya
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Foydalanuvchining Telegram ID va ismiga murojaat qilish
    user_id = update.message.from_user.id
    user_name = update.message.from_user.first_name
    await update.message.reply_text(f"Salom, {user_name}! Sizning Telegram ID'ingiz: {user_id}")


# Botni ishga tushirish
async def main():
    application = Application.builder().token(TOKEN).build()

    # /start komandasi uchun handler
    application.add_handler(CommandHandler("start", start))

    # Botni ishga tushurish
    await application.run_polling()


# Asosiy funktsiyani chaqirish
if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
