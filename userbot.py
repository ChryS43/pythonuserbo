from telethon.sync import TelegramClient, events
import asyncio

api_id = 8339070
api_hash = "f65352465cb4bc25779336627a19112d"

loop = asyncio.get_event_loop()

with TelegramClient('name', api_id, api_hash) as client:

    async def send_multiple_message():
        while True:
            await client.send_message('me', 'Hello, myself!')
            await asyncio.sleep(3)

    loop.create_task(send_multiple_message())
    client.run_until_disconnected()