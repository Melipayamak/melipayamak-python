import zeep
from zeep.transports import AsyncTransport
import asyncio


class ContactsAsync:
    PATH = "http://api.payamak-panel.com/post/contacts.asmx?wsdl"

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

    def add_group(self, groupName, Descriptions, showToChilds):
        data = {
            'groupName': groupName,
            'Descriptions': Descriptions,
            'showToChilds': showToChilds
        }
        return self.makeRequest('AddGroup', {**self.get_data(), **data})
        

    def add(self, options):
        return self.makeRequest('AddContact', {**self.get_data(), **options})
        

    def check_mobile_exist(self, mobileNumber):
        data = {
            'mobileNumber': mobileNumber
        }
        return self.makeRequest('CheckMobileExistInContact', {**self.get_data(), **data})


    def get(self, groupId, keyword, _from, count):
        data = {
            'groupId': groupId,
            'keyword': keyword,
            'from': _from,
            'count': count

        }
        return self.makeRequest('GetContacts', {**self.get_data(), **data})
        

    def get_groups(self):
        return self.makeRequest('GetGroups', self.get_data())


    def change(self, options):
        return self.makeRequest('ChangeContact', {**self.get_data(), **options})


    def remove(self, mobilenumber):
        data = {
            'mobileNumber': mobilenumber
        }
        return self.makeRequest('RemoveContact', {**self.get_data(), **data})
        

    def get_events(self, contactId):
        data = {
            'contactId': contactId
        }
        return self.makeRequest('GetContactEvents', {**self.get_data(), **data})
        
