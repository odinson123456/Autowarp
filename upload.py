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
        await app.send_message(chat_id=chat, text=filejs, parse_mode=ParseMode.MARKDOWN)
        for data in json.loads(open("otp.json").read()).values():
            logslnk = await paste(data["logs"])
            try:
                await app.send_document(
                    chat_id=chat,
                    document=data["outfile"],
                    caption=data["name"] + "\n\nLogs : " + logslnk,
                    file_name=f"{data['name']}.apk",
                )
            except:
                traceback.print_exc()

uvloop.install()
asyncio.run(main())
