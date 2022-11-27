from typing import Coroutine

import aiohttp


async def get(url: str) -> Coroutine:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()
