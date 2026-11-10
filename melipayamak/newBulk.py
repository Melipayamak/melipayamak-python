from zeep import Client


class NewBulk:
    PATH = 'http://api.payamak-panel.com/post/newbulks.asmx?wsdl'

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.client = Client(self.PATH)

    def get_data(self):
        return {
            'username': self.username,
            'password': self.password
        }

    def add_number_bulk(self, _from, title, message, receivers, dateToSend):
        data = {
            'from': _from,
            'title': title,
            'message': message,
            'receivers': receivers,
            'DateToSend': dateToSend
        }
        return self.client.service.AddNumberBulk(**self.get_data(), **data)

    def add_number_bulk2(self, _from, body, to):
        data = {
            'from': _from,
            'body': body,
            'to': to
        }
        return self.client.service.AddNumberBulk2(**self.get_data(), **data)

    def get_bulk_deliveries(self, recIds):
        return self.client.service.GetBulkDeliveries(**self.get_data(), recIds=recIds)

    def get_bulk_deliveries2(self, recId):
        return self.client.service.GetBulkDeliveries2(**self.get_data(), recId=recId)

    def get_bulk_details(self, bulkId):
        return self.client.service.GetBulkDetails(**self.get_data(), bulkId=bulkId)
    
    def send_sms_to_contact(self, message, title, _from, groupId, dateToSend):
        data = {
            'message': message,
            'title': title,
            'from': _from,
            'groupId': groupId,
            'dateToSend': dateToSend
        }
        return self.client.service.SendSmsToContact(**self.get_data(), **data)