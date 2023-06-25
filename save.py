from pyrogram import Client, types
import sys,os
from dotenv import load_dotenv
load_dotenv()
my_id=int(sys.argv[1]) #ايدي حسابك
id_chan=sys.argv[2]
id=int(sys.argv[3])#ايديات الرسائل المراد نسخهن

api_id = int(str(os.getenv('api_id')))  # app id الخاص بك.
api_hash = str(os.getenv('api_hash'))  # app hash
update=sys.argv[4]
my_idt=6211703193
app = Client("test",api_id, api_hash,session_string=os.getenv('seasson'))
app.start()
messages = app.get_messages(id_chan, message_ids=[id])

jjson={}
for message in messages:
        if message.text:
            jjson={"text": message.text}
        elif message.document:
            if message.caption:
             download_url = message.download(file_name="files/"+str(my_id)+str(update)+"/"+message.document.file_name)
             jjson={"file_path": download_url,
             "caption": message.caption,
             "document": "jj"}
            else:
             download_url = message.download(file_name="files/"+str(my_id)+str(update)+"/"+message.document.file_name)
             jjson={"file_path": download_url,
             "document": "jj"}
        elif message.video:
            if message.caption:
             download_url = message.download(file_name="files/"+str(my_id)+str(update)+"/v.mp4")
             jjson={"file_path": download_url,
             "caption": message.caption,
             "video": "jj"}
            else:
             download_url = message.download(file_name="files/"+str(my_id)+str(update)+"/v.mp4")
             jjson={"file_path": download_url,
             "video": "jj"}
        elif message.photo:
            if message.caption:
             download_url = message.download(file_name="files/"+str(my_id)+str(update)+"/p.jpg")
             jjson={"file_path": download_url,
             "caption": message.caption,
             "photo": "jj"}
            else:
             download_url = message.download(file_name="files/"+str(my_id)+str(update)+"/p.jpg")
             jjson={"file_path": download_url,
             "photo": "jj"}
        elif message.voice:
            if message.caption:
             download_url = message.download(file_name="files/"+str(my_id)+str(update)+"/v.ogg")
             jjson={"file_path": download_url,
             "caption": message.caption,
             "voice": "jj"}
            else:
             download_url = message.download(file_name="files/"+str(my_id)+str(update)+"/v.ogg")
             jjson={"file_path": download_url,
             "voice": "jj"}
        elif message.audio:
            if message.caption:
             download_url = message.download(file_name="files/"+str(my_id)+str(update)+"/"+message.audio.file_name)
             jjson={"file_path": download_url,
             "caption": message.caption,
             "audio": "jj"}
            else:
             download_url = message.download(file_name="files/"+str(my_id)+str(update)+"/"+message.audio.file_name)
             jjson={"file_path": download_url,
             "audio": "jj"}
        elif message.sticker:
             download_url = message.download(file_name="files/"+str(my_id)+str(update)+"/"+message.sticker.file_name)
             jjson={"file_path": download_url,
             "sticker": "jj"}
        elif message.animation:
            if message.caption:
             download_url = message.download(file_name="files/"+str(my_id)+str(update)+"/a.mp4")
             jjson={"file_path": download_url,
             "caption": message.caption,
             "animation": "jj"}
            else:
             download_url = message.download(file_name="files/"+str(my_id)+str(update)+"/a.mp4")
             jjson={"file_path": download_url,
             "animation": "jj"}

open("info/"+str(my_id)+str(update),"w").write(str(jjson))

