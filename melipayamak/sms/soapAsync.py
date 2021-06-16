import zeep
from zeep.transports import AsyncTransport
import asyncio
# import time

class SoapAsync:
    PATH = "http://api.payamak-panel.com/post/%s.asmx?wsdl"

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.sendUrl = self.PATH % ("send")
        self.receiveUrl = self.PATH % ("receive")
        self.voiceUrl = self.PATH % ("Voice")
        self.scheduleUrl = self.PATH % ("Schedule")

    def get_data(self):
        return {
            'username': self.username,
            'password': self.password
        }

    def makeRequest(self, url, func, data):
        result = []

        def handle_future(future):
            result.extend(future.result())

        loop = asyncio.get_event_loop()

        transport = AsyncTransport(loop, cache=None)
        client = zeep.Client(url, transport=transport)

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




    def get_credit(self):
        return self.makeRequest(self.sendUrl, 'GetCredit', self.get_data())

    def is_delivered(self, recId):
        
        if isinstance(recId, list):
            data = { 'recIds': recId }
            return self.makeRequest(self.sendUrl, 'GetDeliveries', {**data, **self.get_data()})
        else:
            data = { 'recId': recId }
            return self.makeRequest(self.sendUrl, 'GetDelivery', self.get_data())

    def send(self, to, _from, text, isflash=False):
        data = {
            'from': _from,
            'text': text,
            'isflash': isflash,
            'to': to
        }

        if isinstance(to, list):
            return self.makeRequest(self.sendUrl, 'SendSimpleSMS', {**data, **self.get_data()})
        else:
            return self.makeRequest(self.sendUrl, 'SendSimpleSMS2', {**data, **self.get_data()})

    def send2(self, to, _from, text, isflash=False, udh=''):
        to = to if isinstance(to, list) else [to]
        data = {
            'from': _from,
            'text': text,
            'isflash': isflash,
            'to': to,
            'udh': udh
        }
        return self.makeRequest(self.sendUrl, 'SendSms', {**data, **self.get_data()})

    def send_with_domain(self, to, _from, text, isflash, domainName):
        data = {
            'from': _from,
            'text': text,
            'isflash': isflash,
            'to': to,
            'domainName': domainName
        }
        return self.makeRequest(self.sendUrl, 'SendWithDomain', {**data, **self.get_data()})

    def send_by_base_number(self, text, to, bodyId):
        data = {
            'text': text,
            'to': to,
            'bodyId': bodyId
        }
        
        if isinstance(text, list):
            return self.makeRequest(self.sendUrl, 'SendByBaseNumber', {**data, **self.get_data()})
        else:
            return self.makeRequest(self.sendUrl, 'SendByBaseNumber2', {**data, **self.get_data()})
    
    def get_messages(self, location, index, count, _from=''):
        data = {
            'location': location,
            'index': index,
            'count': count,
            'from': _from
        }
        return self.makeRequest(self.sendUrl, 'getMessages', {**data, **self.get_data()})


    def get_messages_str(self, location, index, count, _from=''):
        data = {
            'location': location,
            'index': index,
            'count': count,
            'from': _from
        }
        return self.makeRequest(self.receiveUrl, 'GetMessageStr', {**data, **self.get_data()})

    def get_messages_by_date(self, location, index, count, dateFrom, dateTo, _from=''):
        data = {
            'location': location,
            'index': index,
            'count': count,
            'from': _from,
            'dateFrom': dateFrom,
            'dateTo': dateTo
        }
        return self.makeRequest(self.receiveUrl, 'GetMessagesByDate', {**data, **self.get_data()})

    def get_messages_receptions(self, msgId, fromRows):
        data = {
            'msgId': msgId,
            'fromRows': fromRows
        }
        return self.makeRequest(self.receiveUrl, 'GetMessagesReceptions', {**data, **self.get_data()})

    def get_users_messages_by_date(self, location, index, count, _from,dateFrom, dateTo):
        data = {
            'location': location,
            'index': index,
            'count': count,
            'from': _from,
            'dateFrom': dateFrom,
            'dateTo': dateTo
        }
        return self.makeRequest(self.receiveUrl, 'GetUsersMessagesByDate', {**data, **self.get_data()})

    def remove(self, msgIds):
        data = {
            'msgIds': msgIds,
        }
        return self.makeRequest(self.receiveUrl, 'RemoveMessages2', {**data, **self.get_data()})

    def get_price(self, irancellCount, mtnCount,  _from, text):
        data = {
            'irancellCount': irancellCount,
            'mtnCount': mtnCount,
            'text': text,
            'from': _from
        }
        return self.makeRequest(self.sendUrl, 'GetSmsPrice', {**data, **self.get_data()})

    def get_inbox_count(self, isRead=False):
        data = {
            'isRead': isRead,
        }
        return self.makeRequest(self.sendUrl, 'GetInboxCount', {**data, **self.get_data()})

    def send_with_speech(self, to, _from, text, speech):
        data = {
            'to': to,
            'from': _from,
            'smsBody': text,
            'speechBody': speech
        }
        return self.makeRequest(self.voiceUrl, 'SendSMSWithSpeechText', {**data, **self.get_data()})

    def send_with_speech_schdule_date(self, to, _from, text, speech, scheduleDate):
        data = {
            'to': to,
            'from': _from,
            'smsBody': text,
            'speechBody': speech,
            'scheduleDate': scheduleDate
        }
        return self.makeRequest(self.voiceUrl, 'SendSMSWithSpeechTextBySchduleDate', {**data, **self.get_data()})

    def get_send_with_speech(self, recId):
        data = {
            'recId': recId
        }
        return self.makeRequest(self.voiceUrl, 'GetSendSMSWithSpeechTextStatus', {**data, **self.get_data()})

    def get_multi_delivery(self, recId):
        data = {
            'recId': recId
        }
        return self.makeRequest(self.sendUrl, 'GetMultiDelivery2', {**data, **self.get_data()})

    def send_multiple_schedule(self, to, _from, text, isflash, scheduleDateTime, period):
        data = {
            'to': to,
            'from': _from,
            'text': text,
            'isflash': isflash,
            'scheduleDateTime': scheduleDateTime,
            'period': period
        }
        return self.makeRequest(self.scheduleUrl, 'AddMultipleSchedule', {**data, **self.get_data()})

    def send_schedule(self, to, _from, text, isflash, scheduleDateTime, period):
        data = {
            'to': to,
            'from': _from,
            'text': text,
            'isflash': isflash,
            'scheduleDateTime': scheduleDateTime,
            'period': period
        }
        return self.makeRequest(self.scheduleUrl, 'AddSchedule', {**data, **self.get_data()})

    def get_schedule_status(self, scheduleId):
        data = {
            'scheduleId': scheduleId
        }
        return self.makeRequest(self.scheduleUrl, 'GetScheduleStatus', {**data, **self.get_data()})

    def remove_schedule(self, scheduleId):
        data = {
            'scheduleId': scheduleId
        }
        return self.makeRequest(self.scheduleUrl, 'RemoveSchedule', {**data, **self.get_data()})

    def add_usance(self, to, _from, text, isflash, scheduleStartDateTime, repeatAfterDays, scheduleEndDateTime):
        data = {
            'to': to,
            'from': _from,
            'text': text,
            'isflash': isflash,
            'scheduleStartDateTime': scheduleStartDateTime,
            'repeatAfterDays': repeatAfterDays,
            'scheduleEndDateTime': scheduleEndDateTime
        }
        return self.makeRequest(self.scheduleUrl, 'AddUsance', {**data, **self.get_data()})
