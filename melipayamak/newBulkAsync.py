import httpx
import zeep
from zeep.transports import AsyncTransport


class NewBulkAsync:
    PATH = 'http://api.payamak-panel.com/post/newbulks.asmx?wsdl'

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


    async def add_number_bulk(self, _from, title, message, receivers, dateToSend):
        data = {
            'from': _from,
            'title': title,
            'message': message,
            'receivers': receivers,
            'DateToSend': dateToSend
        }
        return await self.makeRequest('AddNumberBulk', {**self.get_data(), **data})

    async def add_number_bulk2(self, _from, body, to):
        data = {
            'from': _from,
            'body': body,
            'to': to
        }
        return await self.makeRequest('AddNumberBulk2', {**self.get_data(), **data})

    async def get_bulk_deliveries(self, recIds):
        return await self.makeRequest('GetBulkDeliveries', {**self.get_data(), 'recIds': recIds})

    async def get_bulk_deliveries2(self, recId):
        return await self.makeRequest('GetBulkDeliveries2', {**self.get_data(), 'recId': recId})

    async def get_bulk_details(self, bulkId):
        return await self.makeRequest('GetBulkDetails', {**self.get_data(), 'bulkId': bulkId})
    
    async def send_sms_to_contact(self, message, title, _from, groupId, dateToSend):
        data = {
            'message': message,
            'title': title,
            'from': _from,
            'groupId': groupId,
            'dateToSend': dateToSend
        }
        return await self.makeRequest('SendSmsToContact', {**self.get_data(), **data})
        

    