import httpx


async def get_caihong_data() -> str:
    url = 'https://api.muxiaoguo.cn/api/caihongpi'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        data = resp.json()['data']
        msg = data['comment']
        return msg