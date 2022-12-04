import constants as keys
from telegram.ext import *
import responses as r

print ("bot started")


def start_command(update, context):
    update.message.reply_text("هذا البوت يقدّم خدمة تصريف الأفعال بالاعتماد على خدمة قطرب. أدخل الفعل والزمن بهذه الصيغة: صنع في المضارع"
                              )
def handle_message(update, context):
    response = r.sample_responses(update.message.text)
    update.message.reply_text(response)
def main():
    updater = Updater(keys.api_key)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    #dp.add_handler(CommandHandler("h"), second_command)
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    updater.start_polling()
    updater.idle()
main()
