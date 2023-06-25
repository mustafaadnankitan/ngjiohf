import urllib.request, json,requests
import os
import os.path
import glob
import re,time
import ast
from collections import namedtuple
import telegram
from typing import Tuple, Optional
from telegram import Update, Chat, ChatMember, ChatMemberUpdated, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    ChatMemberHandler,
    MessageHandler,
    CallbackQueryHandler,
    Filters,
)
a=0
import logging
import sys
import subprocess
import threading
from dotenv import load_dotenv
channel=False
import random
import string
load_dotenv()
my_path=os.path.dirname(os.path.realpath(__file__))
import re

def is_link(text):
    regex_pattern = "^http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|(?:[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F])))+$"
    return re.match(regex_pattern, text) is not None

if os.getenv('5099437038:AAE3SoMSiz9TDj-rSlPwFzT40qNXwmOBP5s')!=None:
    
    def send_files(text, chat_id, update, context):
     
     list_link= text.replace("E","e").replace("M","m").replace("T","t").split("t.me/")[1].split("/")
     if len(list_link)==2:
      user_ch=list_link[0]
      id_msg=int(list_link[1])


      
      

      letters = string.ascii_letters
      result_str = ''.join(random.choice(letters) for i in range(15))
      os.system(f"python3.8 save.py {chat_id} {user_ch} {id_msg} '{result_str}'")
      name_file=str(chat_id)+str(result_str)
      ttext=open(f"info/{name_file}","r").read()
      
      messagee = json.loads(str(ttext).replace("'","\""))
      
      my_id=chat_id
      if "text" in messagee:
          context.bot.send_message(my_id, messagee["text"])
      elif "document" in messagee:
          if "caption" in messagee:
           context.bot.send_document(my_id, open(messagee["file_path"],"rb"),caption=messagee["caption"])
          else:
           context.bot.send_document(my_id, open(messagee["file_path"],"rb"))
      elif "video" in messagee:
          if "caption" in messagee:
           context.bot.send_video(my_id, open(messagee["file_path"],"rb"),caption=messagee["caption"])
          else:
           context.bot.send_video(my_id, open(messagee["file_path"],"rb"))
      elif "photo" in messagee:
          if "caption" in messagee:
           context.bot.send_photo(my_id, open(messagee["file_path"],"rb"),caption=messagee["caption"])
          else:
           context.bot.send_photo(my_id, open(messagee["file_path"],"rb"))
      elif "voice" in messagee:
          if "caption" in messagee:
           context.bot.send_voice(my_id, open(messagee["file_path"],"rb"),caption=messagee["caption"])
          else:
           context.bot.send_voice(my_id, open(messagee["file_path"],"rb"))
      elif "audio" in messagee:
          if "caption" in messagee:
           context.bot.send_audio(my_id, open(messagee["file_path"],"rb"),caption=messagee["caption"])
          else:
           context.bot.send_audio(my_id, open(messagee["file_path"],"rb"))
      elif "sticker" in messagee:
           context.bot.send_message(chat_id=update.effective_chat.id, text="""لا داعي لكي احضر الاستيكر
تستطيع حفظه بدون الحاجة لي""")
      elif "animation" in messagee:
          if "caption" in messagee:
           context.bot.send_animation(my_id, open(messagee["file_path"],"rb"),caption=messagee["caption"])
          else:
           context.bot.send_animation(my_id, open(messagee["file_path"],"rb"))
      os.system("rm -rf /files/"+str(chat_id)+str(result_str))
      os.system("rm -rf /info/"+str(chat_id)+str(result_str))
     else:
      context.bot.send_message(chat_id=update.effective_chat.id, text="""ارسل رابط المنشور وليس رابط القناة فضلا❤""")
    def mentionss(update: Update, context: CallbackContext):
     
     if update.message.text=="/start":
      chat_id = update.message.chat_id
      

      context.bot.send_message(chat_id=update.effective_chat.id, text="""اهلا بك في بوت جلب رساله من قناة مقيد محتواها
فقط ارسل لي رابط المنشور وسوف احضره
ملاحظه:- تعمل فقط مع القنواة العامة

قناتنا:- @hmsfails""")
     else:
      if is_link(update.message.text):
       context.bot.send_message(chat_id=update.effective_chat.id, text="""لحظه من فضلك❤""")
       send_files(update.message.text,update.effective_chat.id,update,context)
      else:
       a=update.message.text.replace("E","e").replace("M","m").split(".me")[0]
       if a=="t" or a=="T":
        context.bot.send_message(chat_id=update.effective_chat.id, text="""لحظه من فضلك❤""")
        send_files(update.message.text,update.effective_chat.id,update,context)
       else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="""ارسل لي رابط بدون نصوص فضلا❤""")

    try:
        updater = Updater(token=os.getenv('TOKEN'), use_context=True)
    except:
        print("Invalid token exception")
        quit()
    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    def user(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, text=update.effective_chat.id)
    
    user_handler = CommandHandler('user', user)
    dispatcher.add_handler(user_handler)
    from telegram.ext import MessageFilter

    class helpFilter(MessageFilter):
        def filter(self, message):
            return message.text != '/user'

    help_filter = helpFilter()

    def help(update: Update, context: CallbackContext):
          t = threading.Thread(target = mentionss,args = (update,context))
          t.start()
    help_handler = MessageHandler(help_filter, help)
    dispatcher.add_handler(help_handler)
    updater.start_polling()
else:
    print('env error')