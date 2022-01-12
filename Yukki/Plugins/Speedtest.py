import os

import speedtest
import wget
from pyrogram import Client, filters
from pyrogram.types import Message

from Yukki import BOT_ID, SUDOERS, app
from Yukki.Utilities.formatters import bytes

__MODULE__ = "Speedtest"
__HELP__ = """

/speedtest 
- Kiểm tra độ trễ và tốc độ của máy chủ.

"""


@app.on_message(filters.command("speedtest") & ~filters.edited)
async def statsguwid(_, message):
    m = await message.reply_text("Kiểm tra tốc độ chạy")
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = await m.edit("Chạy SpeedTest Tải xuống")
        test.download()
        m = await m.edit("Chạy Kiểm tra tốc độ tải lên")
        test.upload()
        test.results.share()
        result = test.results.dict()
    except Exception as e:
        return await m.edit(e)
    m = await m.edit("Chia sẻ kết quả kiểm tra tốc độ")
    path = wget.download(result["share"])

    output = f"""**Speedtest Results**
    
<u>**Khách hàng:**</u>
**__ISP:__** {result['client']['isp']}
**__Quốc gia:__** {result['client']['country']}
  
<u>**Máy Chủ:**</u>
**__Tên:__** {result['server']['name']}
**__Quốc gia:__** {result['server']['country']}, {result['server']['cc']}
**__Nhà tài trợ:__** {result['server']['sponsor']}
**__Độ trễ:__** {result['server']['latency']}  
**__Ping:__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=path, caption=output
    )
    os.remove(path)
    await m.delete()
