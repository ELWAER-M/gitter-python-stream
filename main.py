import os
import asyncio
import aiohttp

token = os.environ.get("TOKEN")
room_id = os.environ.get("ROOM_ID")

headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

async def main():
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(f"https://stream.gitter.im/v1/rooms/{room_id}/chatMessages") as res:
            async for check in res.content:
                msg = check.decode("utf-8")
                if msg != " \n": print(msg)

loop.create_task(main())
loop.run_forever()
