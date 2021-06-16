import zeep
from zeep.transports import AsyncTransport
import asyncio


class BranchAsync:
    PATH = "http://api.payamak-panel.com/post/Actions.asmx?wsdl"

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


    def get(self, owner):
        data = {
            'owner': owner
        }
        return self.makeRequest('GetBranchs', {**self.get_data(), **data})

    def remove(self, branchId):
        data = {
            'branchId': branchId
        }
        return self.makeRequest('RemoveBranch', {**self.get_data(), **data})

    def add(self, branchName, owner):
        data = {
            'branchName': branchName,
            'owner': owner
        }
        return self.makeRequest('AddBranch', {**self.get_data(), **data})
        

    def add_number(self, mobileNumbers, branchId):
        data = {
            'mobileNumbers': mobileNumbers,
            'branchId': branchId
        }
        return self.makeRequest('AddNumber', {**self.get_data(), **data})
        

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
        return self.makeRequest('AddBulk', {**self.get_data(), **data})
        

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
        return self.makeRequest('AddBulk2', {**self.get_data(), **data})
        

    def get_bulk_count(self, branch, rangeFrom, rangeTo):
        data = {
            'branch': branch,
            'rangeFrom': rangeFrom,
            'rangeTo': rangeTo
        }
        return self.makeRequest('GetBulkCount', {**self.get_data(), **data})
        

    def get_bulk_receptions(self, bulkId, fromRows):
        data = {
            'bulkId': bulkId,
            'fromRows': fromRows
        }
        return self.makeRequest('GetBulkReceptions', {**self.get_data(), **data})
        

    def get_bulk_status(self, bulkId):
        data = {
            'bulkId': bulkId
        }
        return self.makeRequest('GetBulkStatus', {**self.get_data(), **data})
        

    def get_today_sent(self):
        return self.makeRequest('GetTodaySent', self.get_data())


    def get_total_sent(self):
        return self.makeRequest('GetTotalSent', self.get_data())
        

    def remove_bulk(self, bulkId):
        data = {
            'bulkId': bulkId
        }
        return self.makeRequest('RemoveBulk', {**self.get_data(), **data})
        

    def send_multiple_sms(self, to, _from, text, isflash, udh):
        data = {
            'to': to,
            'from': _from,
            'text': text,
            'isflash': isflash,
            'udh': udh
        }
        
        if isinstance(_from, list):
            return self.makeRequest('SendMultipleSMS2', {**self.get_data(), **data})
            
        else:
            return self.makeRequest('SendMultipleSMS', {**self.get_data(), **data})
        

    def update_bulk_delivery(self, bulkId):
        data = {
            'bulkId': bulkId
        }
        return self.makeRequest('UpdateBulkDelivery', {**self.get_data(), **data})
