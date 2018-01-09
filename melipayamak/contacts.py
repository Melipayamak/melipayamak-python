from zeep import Client


class Contacts:
    PATH = "http://api.payamak-panel.com/post/contacts.asmx?wsdl"

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.client = Client(self.PATH)

    def get_data(self):
        return {
            'username': self.username,
            'password': self.password
        }

    def add_group(self, groupName, Descriptions, showToChilds):
        data = {
            'groupName': groupName,
            'Descriptions': Descriptions,
            'showToChilds': showToChilds
        }
        result = self.client.service.AddGroup(**self.get_data(), **data)
        return result

    def add(self, options):
        result = self.client.service.AddContact(**self.get_data(), **options)
        return result

    def check_mobile_exist(self, mobileNumber):
        data = {
            'mobileNumber': mobileNumber
        }
        result = self.client.service.CheckMobileExistInContact(
            **self.get_data(), **data)
        return result

    def get(self, groupId, keyword, _from, count):
        data = {
            'groupId': groupId,
            'keyword': keyword,
            'from': _from,
            'count': count

        }
        result = self.client.service.GetContacts(**self.get_data(), **data)
        return result

    def get_groups(self):
        result = self.client.service.GetGroups(**self.get_data())
        return result

    def change(self, options):
        result = self.client.service.ChangeContact(**self.get_data(), **options)
        return result

    def remove(self, mobilenumber):
        data = {
            'mobileNumber': mobilenumber
        }
        result = self.client.service.RemoveContact(**self.get_data(), **data)
        return result

    def get_events(self, contactId):
        data = {
            'contactId': contactId
        }
        result = self.client.service.GetContactEvents(**self.get_data(), **data)
        return result
