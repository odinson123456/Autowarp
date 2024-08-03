import asyncio
import uvloop
import json
from os import getenv
from pyrogram import Client
from pyrogram.enums import ParseMode
from telegraph import  Telegraph

def uplog(title,logs):
    short_name = "Rev Logger"
    user = Telegraph().create_account(short_name=short_name)
    access_token = user.get("access_token")
    content = logs
    content = content.replace("\n", "<br>")
    response = Telegraph(access_token=access_token).create_page(
        title=title,
        html_content=content,
        author_name=str("Logger"),
        author_url="https://github.com/odinson123456/Autowarp",
    )
    path = response["path"]
    lnk = f"https://graph.org/{path}"
    return lnk

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
        for apk in json.loads(open("logs.json").read()):
            try:
                await app.send_document(
                    chat_id=chat,
                    document=f"out/{apk['filename']}",
                    caption=apk["title"] + "\n\nLogs : "+uplog(apk["title"],apk["logs"]),
                    file_name="YoutubeRevanced.apk"
                )
            except Exception as e:
                print(e)

uvloop.install()
asyncio.run(main())