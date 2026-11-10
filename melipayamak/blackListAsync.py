import httpx
import zeep
from zeep.transports import AsyncTransport


class BlackListAsync:
    PATH = "http://api.payamak-panel.com/post/blacklist.asmx?wsdl"

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def get_data(self):
        return {
            'username': self.username,
            'password': self.password
        }

    async def makeRequest(self, func, data):
        # Zeep uses the synchronous client to load the WSDL and imported
        # schemas, and the asynchronous client for SOAP operations.
        wsdl_client = httpx.Client(follow_redirects=True)
        async_client = httpx.AsyncClient(follow_redirects=True)

        transport = AsyncTransport(
            client=async_client,
            wsdl_client=wsdl_client,
            cache=None,
        )

        try:
            client = zeep.AsyncClient(self.PATH, transport=transport)
            operation = getattr(client.service, func)
            return await operation(**data)
        finally:
            await transport.aclose()


    async def add_black_list(self, number, type):
        data = {
            'number': number,
            'type': type
        }
        return await self.makeRequest('AddBlackList', {**self.get_data(), **data})

    async def add_mobile(self, listId, type, mobileNumbers, addBySms):
        data = {
            'listId': listId,
            'type': type,
            'mobileNumbers': mobileNumbers,
            'addBySms': addBySms
        }
        return await self.makeRequest('AddMobile', {**self.get_data(), **data})

    async def get_black_lists(self):
        return await self.makeRequest('GetBlackLists', self.get_data())

    