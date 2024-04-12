from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '7146222220:AAFvvXi5HLiyKneyL55KU9XOo1LAN1QLSDo'
BOT_USERNAME: Final = '@testingpythonbots_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('wlc')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('wlchelp')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('wlccustom')

def handle_responses(text: str) -> str:
    processed: str = text.lower()
    if 'wlc' in processed:
        return 'wlc work'

    if 'test2' in processed:
        return 'work'

    return 'noting'



async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_responses(new_text)
        else:
            return 

    else:
        response: str = handle_responses(text)

    print('Bot:', response)
    await Update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {Update} caused error {context.error}')

if __name__ == '__main__':
    print('starting bot')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    app.add_handler (MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print('polling....')

    app.run_polling(poll_interval=3)