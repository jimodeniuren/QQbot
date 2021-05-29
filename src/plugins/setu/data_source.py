import httpx


async def get_setu(key) -> []:
    url = f"https://api.lolicon.app/setu?apikey=这里填你的API&r18=0&size1200=true&keyword="+key
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        code = resp.json()
        try:
            data = code['data'][0]
            msg = "pid:" + str(data['pid']) + "\n" + "title:" + data['title'] + "\n" \
              + "author:" + data['author'] + "\n" + "url:" + data['url'] + "\n" + \
              "tags:" + str(data['tags'])
            res = [msg, data['url']]
        except Exception as e:
            data = code["code"]
        return data