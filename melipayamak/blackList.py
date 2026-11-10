from zeep import Client


class BlackList:
    PATH = "http://api.payamak-panel.com/post/blacklist.asmx?wsdl"

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.client = Client(self.PATH)

    def get_data(self):
        return {
            'username': self.username,
            'password': self.password
        }

    def add_black_list(self, number, type):
        data = {
            'number': number,
            'type': type
        }
        return self.client.service.AddBlackList(**self.get_data(), **data)

    def add_mobile(self, listId, type, mobileNumbers, addBySms):
        data = {
            'listId': listId,
            'type': type,
            'mobileNumbers': mobileNumbers,
            'addBySms': addBySms
        }
        return self.client.service.AddMobile(**self.get_data(), **data)

    def get_black_lists(self):
        return self.client.service.GetBlackLists(**self.get_data())

    