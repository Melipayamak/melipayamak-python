import httpx
import zeep
from zeep.transports import AsyncTransport


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

    
    async def add_group(self, groupName, Descriptions, showToChilds):
        data = {
            'groupName': groupName,
            'Descriptions': Descriptions,
            'showToChilds': showToChilds
        }
        return await self.makeRequest('AddGroup', {**self.get_data(), **data})
        

    async def add(self, options):
        return await self.makeRequest('AddContact', {**self.get_data(), **options})


    async def add2(self, groupIds, firstname, lastname, gender, corporation, mobilenumber):
        data = {
            'groupIds': groupIds,
            'firstname': firstname,
            'lastname': lastname,
            'gender': gender,
            'corporation': corporation,
            'mobilenumber': mobilenumber
        }
        return await self.makeRequest('AddContact2', {**self.get_data(), **data})

    async def add_contact_events(self, contactId, eventName, eventType, eventDate):
        data = {
            'contactId': contactId,
            'eventName': eventName,
            'eventType': eventType,
            'eventDate': eventDate
        }
        return await self.makeRequest('AddContactEvents', {**self.get_data(), **data})

    async def change_contact2(self, options):
        return await self.makeRequest('ChangeContact2', {**self.get_data(), **options})

    async def change_group(self, groupId, groupName, Descriptions, showToChilds, groupStatus):
        data = {
            'groupId': groupId,
            'groupName': groupName,
            'Descriptions': Descriptions,
            'showToChilds': showToChilds,
            'groupStatus': groupStatus
        }
        return await self.makeRequest('ChangeGroup', {**self.get_data(), **data})

    async def remove_contact2(self, contactId, groupId):
        return await self.makeRequest('RemoveContact2', {**self.get_data(), 'contactId':contactId, 'groupId':groupId})

    async def remove_group(self, groupId):
        return await self.makeRequest('RemoveGroup', {**self.get_data(), 'groupId':groupId})
    

    async def check_mobile_exist(self, mobileNumber):
        data = {
            'mobileNumber': mobileNumber
        }
        return await self.makeRequest('CheckMobileExistInContact', {**self.get_data(), **data})


    async def get(self, groupId, keyword, _from, count):
        data = {
            'groupId': groupId,
            'keyword': keyword,
            'from': _from,
            'count': count

        }
        return await self.makeRequest('GetContacts', {**self.get_data(), **data})
        

    async def get_groups(self):
        return await self.makeRequest('GetGroups', self.get_data())


    async def change(self, options):
        return await self.makeRequest('ChangeContact', {**self.get_data(), **options})


    async def remove(self, mobilenumber):
        data = {
            'mobileNumber': mobilenumber
        }
        return await self.makeRequest('RemoveContact', {**self.get_data(), **data})
        

    async def get_events(self, contactId):
        data = {
            'contactId': contactId
        }
        return await self.makeRequest('GetContactEvents', {**self.get_data(), **data})
        
