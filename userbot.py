from dotenv import dotenv_values
from telethon.sync import TelegramClient

config = dotenv_values(".env")
api_id = config['API_ID']
api_hash = config['API_HASH']

with TelegramClient('name', api_id, api_hash) as client:

    def send_multiple_message():
        client.send_message('@lupen1324', 'Hello, myself!')
        # await asyncio.sleep(60*3)

    client.run_until_disconnected()