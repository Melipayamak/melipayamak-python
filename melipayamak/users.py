from zeep import Client


class Users:
    PATH = 'http://api.payamak-panel.com/post/users.asmx?wsdl'

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.client = Client(self.PATH)

    def get_data(self):
        return {
            'username': self.username,
            'password': self.password
        }

    def add_payment(self, options):
        result = self.client.service.AddPayment(**self.get_data(), **options)
        return result

    def add(self, options):
        result = self.client.service.AddUser(**self.get_data(), **options)
        return result

    def add_complete(self, options):
        result = self.client.service.AddUserComplete(
            **self.get_data(), **options)
        return result

    def add_with_location(self, options):
        result = self.client.service.AddUserWithLocation(
            **self.get_data(), **options)
        return result

    def authenticate(self):
        result = self.client.service.AuthenticateUser(**self.get_data())
        return result

    def change_credit(self, amount, description, targetUsername, GetTax):
        data = {
            'amount': amount,
            'description': description,
            'targetUsername': targetUsername,
            'GetTax': GetTax
        }
        result = self.client.service.ChangeUserCredit(**self.get_data(), **data)
        return result

    def forgot_password(self, mobileNumber, emailAddress, targetUsername):
        data = {
            'mobileNumber': mobileNumber,
            'emailAddress': emailAddress,
            'targetUsername': targetUsername
        }
        result = self.client.service.ForgotPassword(**self.get_data(), **data)
        return result

    def get_base_price(self, targetUsername):
        data = {
            'targetUsername': targetUsername
        }
        result = self.client.service.GetUserBasePrice(**self.get_data(), **data)
        return result

    def remove(self, targetUsername):
        data = {
            'targetUsername': targetUsername
        }
        result = self.client.service.RemoveUser(**self.get_data(), **data)
        return result

    def get_credit(self, targetUsername):
        data = {
            'targetUsername': targetUsername
        }
        result = self.client.service.GetUserCredit(**self.get_data(), **data)
        return result

    def get_details(self, targetUsername):
        data = {
            'targetUsername': targetUsername
        }
        result = self.client.service.GetUserDetails(**self.get_data(), **data)
        return result

    def get_numbers(self):
        result = self.client.service.GetUserNumbers(**self.get_data())
        return result

    def get_provinces(self):
        result = self.client.service.GetProvinces(**self.get_data())
        return result

    def get_cities(self, provinceId):
        data = {
            'provinceId': provinceId
        }
        result = self.client.service.GetCities(**self.get_data(), **data)
        return result

    def get_expire_date(self):
        result = self.client.service.GetExpireDate(**self.get_data())
        return result

    def get_transactions(self, targetUsername, creditType, dateFrom, dateTo, keyword):
        data = {
            'targetUsername': targetUsername,
            'creditType': creditType,
            'dateFrom': dateFrom,
            'dateTo': dateTo,
            'keyword': keyword
        }
        result = self.client.service.GetUserTransactions(
            **self.get_data(), **data)
        return result

    def get(self):
        result = self.client.service.GetUsers(**self.get_data())
        return result

    def has_filter(self, text):
        data = {
            'text': text
        }
        result = self.client.service.HasFilter(**self.get_data(), **data)
        return result