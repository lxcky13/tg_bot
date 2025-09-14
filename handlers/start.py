from telegram import Update
from telegram.ext import ContextTypes
import logging

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    name = user.first_name if user and user.first_name else "друг"
    await update.message.reply_text(f"Привет, {name}! Я жив.")
    logger.info("Handled /start from %s", user.id if user else "unknown")