import zeep
from zeep.transports import AsyncTransport
import asyncio


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

    def makeRequest(self, func, data):
        result = []

        def handle_future(future):
            result.extend(future.result())

        loop = asyncio.get_event_loop()

        transport = AsyncTransport(loop, cache=None)
        client = zeep.Client(self.PATH, transport=transport)

        tasks = [
            getattr(client.service, func)(**data)
        ]
        future = asyncio.gather(*tasks, return_exceptions=True)

        future.add_done_callback(handle_future)

        # st = time.time()
        loop.run_until_complete(future)
        loop.run_until_complete(transport.session.close())
        # print("time: %.2f" % (time.time() - st))
        return result


    def add(self, title, content, aws=True):
        data = {
            'title': title,
            'content': content,
            'alertWithSms': aws
        }
        return self.makeRequest('AddTicket', {**self.get_data(), **data})
        

    def get_received(self, ticketOwner, ticketType, keyword):
        data = {
            'ticketOwner': ticketOwner,
            'ticketType': ticketType,
            'keyword': keyword
        }
        return self.makeRequest('GetReceivedTickets', {**self.get_data(), **data})
        

    def get_received_count(self, ticketType):
        data = {
            'ticketType': ticketType,
        }
        return self.makeRequest('GetReceivedTicketsCount', {**self.get_data(), **data})


    def get_sent(self, ticketOwner, ticketType, keyword):
        data = {
            'ticketOwner': ticketOwner,
            'ticketType': ticketType,
            'keyword': keyword
        }
        return self.makeRequest('GetSentTickets', {**self.get_data(), **data})


    def get_sent_count(self, ticketType):
        data = {
            'ticketType': ticketType,
        }
        return self.makeRequest('GetSentTicketsCount', {**self.get_data(), **data})
        

    def response(self, ticketId, _type, content, alertWithSms=True):
        data = {
            'ticketId': ticketId,
            'type': _type,
            'content': content,
            'alertWithSms': alertWithSms
        }
        return self.makeRequest('ResponseTicket', {**self.get_data(), **data})
        
