import zeep
from zeep.transports import AsyncTransport
import asyncio


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


    def add_payment(self, options):
        return self.makeRequest('AddPayment', {**self.get_data(), **options})
        

    def add(self, options):
        return self.makeRequest('AddUser', {**self.get_data(), **options})


    def add_complete(self, options):
        return self.makeRequest('AddUserComplete', {**self.get_data(), **options})
        

    def add_with_location(self, options):
        return self.makeRequest('AddUserWithLocation', {**self.get_data(), **options})
        

    def authenticate(self):
        return self.makeRequest('AuthenticateUser', self.get_data())

    def change_credit(self, amount, description, targetUsername, GetTax):
        data = {
            'amount': amount,
            'description': description,
            'targetUsername': targetUsername,
            'GetTax': GetTax
        }
        return self.makeRequest('ChangeUserCredit', {**self.get_data(), **data})


    def forgot_password(self, mobileNumber, emailAddress, targetUsername):
        data = {
            'mobileNumber': mobileNumber,
            'emailAddress': emailAddress,
            'targetUsername': targetUsername
        }
        return self.makeRequest('ForgotPassword', {**self.get_data(), **data})


    def get_base_price(self, targetUsername):
        data = {
            'targetUsername': targetUsername
        }
        return self.makeRequest('GetUserBasePrice', {**self.get_data(), **data})


    def remove(self, targetUsername):
        data = {
            'targetUsername': targetUsername
        }
        return self.makeRequest('RemoveUser', {**self.get_data(), **data})


    def get_credit(self, targetUsername):
        data = {
            'targetUsername': targetUsername
        }
        return self.makeRequest('GetUserCredit', {**self.get_data(), **data})


    def get_details(self, targetUsername):
        data = {
            'targetUsername': targetUsername
        }
        return self.makeRequest('GetUserDetails', {**self.get_data(), **data})


    def get_numbers(self):
        return self.makeRequest('GetUserNumbers', self.get_data())
        

    def get_provinces(self):
        return self.makeRequest('GetProvinces', self.get_data())
        

    def get_cities(self, provinceId):
        data = {
            'provinceId': provinceId
        }
        return self.makeRequest('GetCities', {**self.get_data(), **data})


    def get_expire_date(self):
        return self.makeRequest('GetExpireDate', self.get_data())
        

    def get_transactions(self, targetUsername, creditType, dateFrom, dateTo, keyword):
        data = {
            'targetUsername': targetUsername,
            'creditType': creditType,
            'dateFrom': dateFrom,
            'dateTo': dateTo,
            'keyword': keyword
        }
        return self.makeRequest('GetUserTransactions', {**self.get_data(), **data})
        

    def get(self):
        return self.makeRequest('GetUsers', self.get_data())
        

    def has_filter(self, text):
        data = {
            'text': text
        }
        return self.makeRequest('HasFilter', {**self.get_data(), **data})
