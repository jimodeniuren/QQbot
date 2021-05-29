import httpx


async def get_joke_data() -> str:
    url = 'https://api.muxiaoguo.cn/api/xiaohua'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        data = resp.json()
        result = data['data']['content']
    return result
