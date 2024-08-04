import asyncio
import uvloop
import json
import traceback
from os import getenv
from pyrogram import Client
from pyrogram.enums import ParseMode
from utils import *

async def main():
    app = Client(
        name="bot",
        api_id=int(getenv("API_ID")),
        api_hash=getenv("API_HASH"),
        bot_token=getenv("TOKEN"),
    )
    chat = int(getenv("CHAT"))
    async with app:
        filejs = open("data.txt").read()
        await app.send_message(chat_id=chat, text=filejs,parse_mode=ParseMode.MARKDOWN)
        apk =  json.loads(open("logs.json").read())[0]
        logslnk = await paste(apk['logs'])
        try:
            await app.send_document(
                chat_id=chat,
                document=f"out/{apk['filename']}",
                caption=apk["title"] + "\n\nLogs : "+logslnk,
                file_name="YoutubeRevanced.apk"
            )
        except Exception as e:
            traceback.print_exc()

uvloop.install()
asyncio.run(main())