import httpx
import zeep
from zeep.transports import AsyncTransport


class SmartAsync:
    PATH = "http://api.payamak-panel.com/post/Smartsms.asmx?wsdl"

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


    async def get_smart_sms_deliveries(self, ids):
        return await self.makeRequest('GetSmartSMSDeliveries', {**self.get_data(), 'Id': ids})

    async def get_smart_sms_details(self, id):
        return await self.makeRequest('GetSmartSMSDetails', {**self.get_data(), 'Id': id})

    async def send_multiple_smart_sms(self, to, text, _from, fromSupportOne, fromSupportTwo):
        data = {
            'to': to,
            'text': text,
            'from': _from,
            'fromSupportOne': fromSupportOne,
            'fromSupportTwo': fromSupportTwo
        }
        return await self.makeRequest('SendMultipleSmartSMS', {**self.get_data(), **data})

    async def send_smart_sms(self, to, text, _from, fromSupportOne, fromSupportTwo):
        data = {
            'to': to,
            'text': text,
            'from': _from,
            'fromSupportOne': fromSupportOne,
            'fromSupportTwo': fromSupportTwo
        }
        return await self.makeRequest('SendSmartSMS', {**self.get_data(), **data})

    