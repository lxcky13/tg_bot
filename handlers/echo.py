from telegram import Update
from telegram.ext import ContextTypes
import logging

logger = logging.getLogger(__name__)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text if update.message and update.message.text else ""
    await update.message.reply_text(text)
    logger.info("Echoed message from %s: %s", update.effective_user.id if update.effective_user else "unknown", text)
