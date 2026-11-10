import httpx
import zeep
from zeep.transports import AsyncTransport


class UsersAsync:
    PATH = 'http://api.payamak-panel.com/post/users.asmx?wsdl'

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


    async def add_payment(self, options):
        return await self.makeRequest('AddPayment', {**self.get_data(), **options})
        

    async def add(self, options):
        return await self.makeRequest('AddUser', {**self.get_data(), **options})


    async def add_complete(self, options):
        return await self.makeRequest('AddUserComplete', {**self.get_data(), **options})
        

    async def add_with_location(self, options):
        return await self.makeRequest('AddUserWithLocation', {**self.get_data(), **options})
        

    async def authenticate(self):
        return await self.makeRequest('AuthenticateUser', self.get_data())

    async def change_credit(self, amount, description, targetUsername, GetTax):
        data = {
            'amount': amount,
            'description': description,
            'targetUsername': targetUsername,
            'GetTax': GetTax
        }
        return await self.makeRequest('ChangeUserCredit', {**self.get_data(), **data})


    async def forgot_password(self, mobileNumber, emailAddress, targetUsername):
        data = {
            'mobileNumber': mobileNumber,
            'emailAddress': emailAddress,
            'targetUsername': targetUsername
        }
        return await self.makeRequest('ForgotPassword', {**self.get_data(), **data})


    async def get_base_price(self, targetUsername):
        data = {
            'targetUsername': targetUsername
        }
        return await self.makeRequest('GetUserBasePrice', {**self.get_data(), **data})


    async def remove(self, targetUsername):
        data = {
            'targetUsername': targetUsername
        }
        return await self.makeRequest('RemoveUser', {**self.get_data(), **data})


    async def get_credit(self, targetUsername):
        data = {
            'targetUsername': targetUsername
        }
        return await self.makeRequest('GetUserCredit', {**self.get_data(), **data})

    async def get_credit2(self):
        return await self.makeRequest('GetUserCredit2', self.get_data())


    async def get_details(self, targetUsername):
        data = {
            'targetUsername': targetUsername
        }
        return await self.makeRequest('GetUserDetails', {**self.get_data(), **data})


    async def get_numbers(self):
        return await self.makeRequest('GetUserNumbers', self.get_data())
        

    async def get_provinces(self):
        return await self.makeRequest('GetProvinces', self.get_data())
        

    async def get_cities(self, provinceId):
        data = {
            'provinceId': provinceId
        }
        return await self.makeRequest('GetCities', {**self.get_data(), **data})


    async def get_expire_date(self):
        return await self.makeRequest('GetExpireDate', self.get_data())

    async def get_en_expire_date(self):
        return await self.makeRequest('GetEnExpireDate', self.get_data())
        

    async def get_transactions(self, targetUsername, creditType, dateFrom, dateTo, keyword):
        data = {
            'targetUsername': targetUsername,
            'creditType': creditType,
            'dateFrom': dateFrom,
            'dateTo': dateTo,
            'keyword': keyword
        }
        return await self.makeRequest('GetUserTransactions', {**self.get_data(), **data})
        

    async def get(self):
        return await self.makeRequest('GetUsers', self.get_data())
        

    async def has_filter(self, text):
        data = {
            'text': text
        }
        return await self.makeRequest('HasFilter', {**self.get_data(), **data})
