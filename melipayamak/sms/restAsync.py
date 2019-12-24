import aiohttp

class RestAsync:
    PATH = "https://rest.payamak-panel.com/api/SendSMS/%s"

    def __init__(self, username, password):
        self.username = username
        self.password = password

    async def post(self, url, data):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as resp:
                if resp.status == 200:
                    return await resp.text()

    def get_data(self):
        return {
            'username': self.username,
            'password': self.password
        }

    async def send(self, to, _from, text, isFlash=False):
        url = self.PATH % ('SendSMS')
        data = {
            'to': to,
            'from': _from,
            'text': text,
            'isFlash': isFlash
        }
        return await self.post(url, {**data, **self.get_data()})

    async def send_by_base_number(self, text, to, bodyId):
        url = self.PATH % ('BaseServiceNumber')
        data = {
            'text': text,
            'to': to,
            'bodyId': bodyId
        }
        return await self.post(url, {**data, **self.get_data()})
    
    async def is_delivered(self, recId):
        url = self.PATH % ('GetDeliveries2')
        data = {
            'recId': recId
        }
        return await self.post(url, {**data, **self.get_data()})

    async def get_messages(self, location, index, count, _from=''):
        url = self.PATH % ('GetMessages')
        data = {
            'location': location,
            'index': index,
            'count': count,
            'from': _from
        }
        return await self.post(url, {**data, **self.get_data()})

    async def get_credit(self):
        url = self.PATH % ('GetCredit')
        return await self.post(url, self.get_data())

    async def get_base_price(self):
        url = self.PATH % ('GetBasePrice')
        return await self.post(url, self.get_data())

    async def get_numbers(self):
        url = self.PATH % ('GetUserNumbers')
        return await self.post(url, self.get_data())
