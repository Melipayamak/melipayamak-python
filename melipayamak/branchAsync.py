import httpx
import zeep
from zeep.transports import AsyncTransport


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


    async def get(self, owner):
        data = {
            'owner': owner
        }
        return await self.makeRequest('GetBranchs', {**self.get_data(), **data})

    async def remove(self, branchId):
        data = {
            'branchId': branchId
        }
        return await self.makeRequest('RemoveBranch', {**self.get_data(), **data})

    async def add(self, branchName, owner):
        data = {
            'branchName': branchName,
            'owner': owner
        }
        return await self.makeRequest('AddBranch', {**self.get_data(), **data})
        

    async def add_number(self, mobileNumbers, branchId):
        data = {
            'mobileNumbers': mobileNumbers,
            'branchId': branchId
        }
        return await self.makeRequest('AddNumber', {**self.get_data(), **data})
        

    async def send_bulk(self, _from, title, message, branch, DateToSend, requestCount, bulkType, rowFrom, rangeFrom, rangeTo):
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
        return await self.makeRequest('AddBulk', {**self.get_data(), **data})
        

    async def sendBulk2(self, _from, title, message, branch, DateToSend, requestCount, bulkType, rowFrom, rangeFrom, rangeTo):
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
        return await self.makeRequest('AddBulk2', {**self.get_data(), **data})
        

    async def get_bulk_count(self, branch, rangeFrom, rangeTo):
        data = {
            'branch': branch,
            'rangeFrom': rangeFrom,
            'rangeTo': rangeTo
        }
        return await self.makeRequest('GetBulkCount', {**self.get_data(), **data})
        

    async def get_bulk_receptions(self, bulkId, fromRows):
        data = {
            'bulkId': bulkId,
            'fromRows': fromRows
        }
        return await self.makeRequest('GetBulkReceptions', {**self.get_data(), **data})
        

    async def get_bulk_status(self, bulkId):
        data = {
            'bulkId': bulkId
        }
        return await self.makeRequest('GetBulkStatus', {**self.get_data(), **data})
        

    async def get_today_sent(self):
        return await self.makeRequest('GetTodaySent', self.get_data())


    async def get_total_sent(self):
        return await self.makeRequest('GetTotalSent', self.get_data())
        

    async def remove_bulk(self, bulkId):
        data = {
            'bulkId': bulkId
        }
        return await self.makeRequest('RemoveBulk', {**self.get_data(), **data})
        

    async def send_multiple_sms(self, to, _from, text, isflash, udh):
        data = {
            'to': to,
            'from': _from,
            'text': text,
            'isflash': isflash,
            'udh': udh
        }
        
        if isinstance(_from, list):
            return await self.makeRequest('SendMultipleSMS2', {**self.get_data(), **data})
            
        else:
            return await self.makeRequest('SendMultipleSMS', {**self.get_data(), **data})
        

    async def update_bulk_delivery(self, bulkId):
        data = {
            'bulkId': bulkId
        }
        return await self.makeRequest('UpdateBulkDelivery', {**self.get_data(), **data})

    async def get_multiple_sms3_deliveries(self, idCollection):
        ids = idCollection if isinstance(idCollection, list) else [idCollection]
        return await self.makeRequest('GetMultipleSMS3Deliveries', {**self.get_data(), 'Id': ids})
    
    async def get_send_bulk(self):
        return await self.makeRequest('GetSendBulk', self.get_data())