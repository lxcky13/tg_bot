from telegram import Update
from telegram.ext import ContextTypes

HELP = (
    "/start — привет\n"
    "/help — показать это сообщение\n"
    "Просто отправь текст — я отвечу."
)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(HELP)