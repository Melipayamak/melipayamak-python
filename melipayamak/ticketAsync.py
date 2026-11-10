import httpx
import zeep
from zeep.transports import AsyncTransport


class TicketAsync:
    PATH = 'http://api.payamak-panel.com/post/Tickets.asmx?wsdl'

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


    async def add(self, title, content, aws=True):
        data = {
            'title': title,
            'content': content,
            'alertWithSms': aws
        }
        return await self.makeRequest('AddTicket', {**self.get_data(), **data})
        

    async def get_received(self, ticketOwner, ticketType, keyword):
        data = {
            'ticketOwner': ticketOwner,
            'ticketType': ticketType,
            'keyword': keyword
        }
        return await self.makeRequest('GetReceivedTickets', {**self.get_data(), **data})
        

    async def get_received_count(self, ticketType):
        data = {
            'ticketType': ticketType,
        }
        return await self.makeRequest('GetReceivedTicketsCount', {**self.get_data(), **data})


    async def get_sent(self, ticketOwner, ticketType, keyword):
        data = {
            'ticketOwner': ticketOwner,
            'ticketType': ticketType,
            'keyword': keyword
        }
        return await self.makeRequest('GetSentTickets', {**self.get_data(), **data})


    async def get_sent_count(self, ticketType):
        data = {
            'ticketType': ticketType,
        }
        return await self.makeRequest('GetSentTicketsCount', {**self.get_data(), **data})
        

    async def response(self, ticketId, _type, content, alertWithSms=True):
        data = {
            'ticketId': ticketId,
            'type': _type,
            'content': content,
            'alertWithSms': alertWithSms
        }
        return await self.makeRequest('ResponseTicket', {**self.get_data(), **data})
        
