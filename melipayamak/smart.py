from zeep import Client


class Smart:
    PATH = "http://api.payamak-panel.com/post/Smartsms.asmx?wsdl"

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.client = Client(self.PATH)

    def get_data(self):
        return {
            'username': self.username,
            'password': self.password
        }

    def get_smart_sms_deliveries(self, ids):
        return self.client.service.GetSmartSMSDeliveries(**self.get_data(), Id=ids)

    def get_smart_sms_details(self, id):
        return self.client.service.GetSmartSMSDetails(**self.get_data(), Id=id)

    def send_multiple_smart_sms(self, to, text, _from, fromSupportOne, fromSupportTwo):
        data = {
            'to': to,
            'text': text,
            'from': _from,
            'fromSupportOne': fromSupportOne,
            'fromSupportTwo': fromSupportTwo
        }
        return self.client.service.SendMultipleSmartSMS(**self.get_data(), **data)

    def send_smart_sms(self, to, text, _from, fromSupportOne, fromSupportTwo):
        data = {
            'to': to,
            'text': text,
            'from': _from,
            'fromSupportOne': fromSupportOne,
            'fromSupportTwo': fromSupportTwo
        }
        return self.client.service.SendSmartSMS(**self.get_data(), **data)
    