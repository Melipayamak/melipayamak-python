from zeep import Client


class Branch:
    PATH = "http://api.payamak-panel.com/post/Actions.asmx?wsdl"

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.client = Client(self.PATH)

    def get_data(self):
        return {
            'username': self.username,
            'password': self.password
        }

    def get(self, owner):
        data = {
            'owner': owner
        }
        result = self.client.service.GetBranchs(**self.get_data(), **data)
        return result

    def remove(self, branchId):
        data = {
            'branchId': branchId
        }
        result = self.client.service.RemoveBranch(**self.get_data(), **data)
        return result

    def add(self, branchName, owner):
        data = {
            'branchName': branchName,
            'owner': owner
        }
        result = self.client.service.AddBranch(**self.get_data(), **data)
        return result

    def add_number(self, mobileNumbers, branchId):
        data = {
            'mobileNumbers': mobileNumbers,
            'branchId': branchId
        }
        result = self.client.service.AddNumber(**self.get_data(), **data)
        return result

    def send_bulk(self, _from, title, message, branch, DateToSend, requestCount, bulkType, rowFrom, rangeFrom, rangeTo):
        data = {
            'from': _from,
            'title': title,
            'message': message,
            'branch': branch,
            'DateToSend': DateToSend,
            'requestCount': requestCount,
            'bulkType': bulkType,
            'rowFrom': rowFrom,
            'rangeFrom': rangeFrom,
            'rangeTo': rangeTo
        }
        result = self.client.service.AddBulk(**self.get_data(), **data)
        return result

    def sendBulk2(self, _from, title, message, branch, DateToSend, requestCount, bulkType, rowFrom, rangeFrom, rangeTo):
        data = {
            'from': _from,
            'title': title,
            'message': message,
            'branch': branch,
            'DateToSend': DateToSend,
            'requestCount': requestCount,
            'bulkType': bulkType,
            'rowFrom': rowFrom,
            'rangeFrom': rangeFrom,
            'rangeTo': rangeTo
        }
        result = self.client.service.AddBulk2(**self.get_data(), **data)
        return result

    def get_bulk_count(self, branch, rangeFrom, rangeTo):
        data = {
            'branch': branch,
            'rangeFrom': rangeFrom,
            'rangeTo': rangeTo
        }
        result = self.client.service.GetBulkCount(**self.get_data(), **data)
        return result

    def get_bulk_receptions(self, bulkId, fromRows):
        data = {
            'bulkId': bulkId,
            'fromRows': fromRows
        }
        result = self.client.service.GetBulkReceptions(
            **self.get_data(), **data)
        return result

    def get_bulk_status(self, bulkId):
        data = {
            'bulkId': bulkId
        }
        result = self.client.service.GetBulkStatus(**self.get_data(), **data)
        return result

    def get_today_sent(self):
        result = self.client.service.GetTodaySent(**self.get_data())
        return result

    def get_total_sent(self):
        result = self.client.service.GetTotalSent(**self.get_data())
        return result

    def remove_bulk(self, bulkId):
        data = {
            'bulkId': bulkId
        }
        result = self.client.service.RemoveBulk(**self.get_data(), **data)
        return result

    def send_multiple_sms(self, to, _from, text, isflash, udh):
        data = {
            'to': to,
            'from': _from,
            'text': text,
            'isflash': isflash,
            'udh': udh
        }
        result = None
        if isinstance(_from, list):
            result = self.client.service.SendMultipleSMS2(
                **self.get_data(), **data)
        else:
            result = self.client.service.SendMultipleSMS(
                **self.get_data(), **data)
        return result

    def update_bulk_delivery(self, bulkId):
        data = {
            'bulkId': bulkId
        }
        result = self.client.service.UpdateBulkDelivery(
            **self.get_data(), **data)
        return result
