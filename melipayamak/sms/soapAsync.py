import httpx
import zeep
from zeep.transports import AsyncTransport


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

    async def makeRequest(self, url, func, data):
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
            client = zeep.AsyncClient(url, transport=transport)
            operation = getattr(client.service, func)
            return await operation(**data)
        finally:
            await transport.aclose()




    async def get_credit(self):
        return await self.makeRequest(self.sendUrl, 'GetCredit', self.get_data())

    async def is_delivered(self, recId):
        
        if isinstance(recId, list):
            data = { 'recIds': recId }
            return await self.makeRequest(self.sendUrl, 'GetDeliveries', {**data, **self.get_data()})
        else:
            data = { 'recId': recId }
            return await self.makeRequest(self.sendUrl, 'GetDelivery', self.get_data())

    async def send(self, to, _from, text, isflash=False):
        data = {
            'from': _from,
            'text': text,
            'isflash': isflash,
            'to': to
        }

        if isinstance(to, list):
            return await self.makeRequest(self.sendUrl, 'SendSimpleSMS', {**data, **self.get_data()})
        else:
            return await self.makeRequest(self.sendUrl, 'SendSimpleSMS2', {**data, **self.get_data()})

    async def send2(self, to, _from, text, isflash=False, udh=''):
        to = to if isinstance(to, list) else [to]
        data = {
            'from': _from,
            'text': text,
            'isflash': isflash,
            'to': to,
            'udh': udh
        }
        return await self.makeRequest(self.sendUrl, 'SendSms', {**data, **self.get_data()})

    async def send_with_domain(self, to, _from, text, isflash, domainName):
        data = {
            'from': _from,
            'text': text,
            'isflash': isflash,
            'to': to,
            'domainName': domainName
        }
        return await self.makeRequest(self.sendUrl, 'SendWithDomain', {**data, **self.get_data()})

    async def send_by_base_number(self, text, to, bodyId):
        data = {
            'text': text,
            'to': to,
            'bodyId': bodyId
        }
        
        if isinstance(text, list):
            return await self.makeRequest(self.sendUrl, 'SendByBaseNumber', {**data, **self.get_data()})
        else:
            return await self.makeRequest(self.sendUrl, 'SendByBaseNumber2', {**data, **self.get_data()})


    async def send_by_base_number3(self, text, to):
        return await self.makeRequest(self.sendUrl, 'SendByBaseNumber3', {**self.get_data(), 'text': text, 'to': to})
        
    
    async def send_by_base_number4(self, text, to, bodyId, smsPrice):
        return await self.makeRequest(self.sendUrl, 'SendByBaseNumber4', {**self.get_data(), 'text': text, 'to': to, 'bodyId': bodyId, 'smsPrice': smsPrice})
    
    
    async def send_otp2(self, to, _from, code):
        return await self.makeRequest(self.sendUrl, 'SendOtp2', {**self.get_data(), 'to': to, 'from': _from, 'code': code})
    
    
    async def send_sms2(self, to, _from, text, isflash=False, udh=''):
        to = to if isinstance(to, list) else [to]
        data = {
            'from': _from,
            'text': text,
            'isflash': isflash,
            'to': to,
            'udh': udh
        }
        return await self.makeRequest(self.sendUrl, 'SendSms2', {**data, **self.get_data()})
    
    
    async def get_messages(self, location, index, count, _from=''):
        data = {
            'location': location,
            'index': index,
            'count': count,
            'from': _from
        }
        return await self.makeRequest(self.sendUrl, 'getMessages', {**data, **self.get_data()})


    async def get_messages_str(self, location, index, count, _from=''):
        data = {
            'location': location,
            'index': index,
            'count': count,
            'from': _from
        }
        return await self.makeRequest(self.receiveUrl, 'GetMessageStr', {**data, **self.get_data()})

    async def get_messages_by_date(self, location, index, count, dateFrom, dateTo, _from=''):
        data = {
            'location': location,
            'index': index,
            'count': count,
            'from': _from,
            'dateFrom': dateFrom,
            'dateTo': dateTo
        }
        return await self.makeRequest(self.receiveUrl, 'GetMessagesByDate', {**data, **self.get_data()})

    async def get_messages_receptions(self, msgId, fromRows):
        data = {
            'msgId': msgId,
            'fromRows': fromRows
        }
        return await self.makeRequest(self.receiveUrl, 'GetMessagesReceptions', {**data, **self.get_data()})

    async def get_users_messages_by_date(self, location, index, count, _from,dateFrom, dateTo):
        data = {
            'location': location,
            'index': index,
            'count': count,
            'from': _from,
            'dateFrom': dateFrom,
            'dateTo': dateTo
        }
        return await self.makeRequest(self.receiveUrl, 'GetUsersMessagesByDate', {**data, **self.get_data()})

    async def remove(self, msgIds):
        data = {
            'msgIds': msgIds,
        }
        return await self.makeRequest(self.receiveUrl, 'RemoveMessages2', {**data, **self.get_data()})

    async def get_price(self, irancellCount, mtnCount,  _from, text):
        data = {
            'irancellCount': irancellCount,
            'mtnCount': mtnCount,
            'text': text,
            'from': _from
        }
        return await self.makeRequest(self.sendUrl, 'GetSmsPrice', {**data, **self.get_data()})

    async def get_inbox_count(self, isRead=False):
        data = {
            'isRead': isRead,
        }
        return await self.makeRequest(self.sendUrl, 'GetInboxCount', {**data, **self.get_data()})

    async def get_outbox_count(self):
        return await self.makeRequest(self.receiveUrl, 'GetOutBoxCount', **self.get_data())

    async def send_with_speech(self, to, _from, text, speech):
        data = {
            'to': to,
            'from': _from,
            'smsBody': text,
            'speechBody': speech
        }
        return await self.makeRequest(self.voiceUrl, 'SendSMSWithSpeechText', {**data, **self.get_data()})

    async def send_with_speech_schdule_date(self, to, _from, text, speech, scheduleDate):
        data = {
            'to': to,
            'from': _from,
            'smsBody': text,
            'speechBody': speech,
            'scheduleDate': scheduleDate
        }
        return await self.makeRequest(self.voiceUrl, 'SendSMSWithSpeechTextBySchduleDate', {**data, **self.get_data()})

    async def get_send_with_speech(self, recId):
        data = {
            'recId': recId
        }
        return await self.makeRequest(self.voiceUrl, 'GetSendSMSWithSpeechTextStatus', {**data, **self.get_data()})

    async def get_send_speech_text_status(self, recId):
        return await self.makeRequest(self.voiceUrl, 'GetSendSpeechTextStatus', {**self.get_data(), 'recId': recId})
    
    async def get_send_speech_text_statuses(self, recIds):
        return await self.makeRequest(self.voiceUrl, 'GetSendSpeechTextStatuses', {**self.get_data(), 'recIds': recIds})
    
    async def send_bulk_speech_text(self, title, body, receivers, dateToSend, repeatCount):
        data = {
            'title': title,
            'body': body,
            'receivers': receivers,
            'DateToSend': dateToSend,
            'RepeatCount': repeatCount
        }
        return await self.makeRequest(self.voiceUrl, 'SendBulkSpeechText', {**self.get_data(), **data})
    
    async def send_bulk_voice_sms(self, title, voiceFileId, receivers, dateToSend, repeatCount):
        data = {
            'title': title,
            'voiceFileId': voiceFileId,
            'receivers': receivers,
            'DateToSend': dateToSend,
            'repeatCount': repeatCount
        }
        return await self.makeRequest(self.voiceUrl, 'SendBulkVoiceSMS', {**self.get_data(), **data})
    
    async def send_speech_text(self, text, to):
        return await self.makeRequest(self.voiceUrl, 'SendSpeechText', {**self.get_data(), 'text':text, 'to':to})
    
    async def send_voice_otp(self, to, code):
        return await self.makeRequest(self.voiceUrl, 'SendVoiceOtp', {**self.get_data(), 'to':to, 'code':code})
    

    async def get_multi_delivery(self, recId):
        data = {
            'recId': recId
        }
        return await self.makeRequest(self.sendUrl, 'GetMultiDelivery2', {**data, **self.get_data()})

    async def send_multiple_schedule(self, to, _from, text, isflash, scheduleDateTime, period):
        data = {
            'to': to,
            'from': _from,
            'text': text,
            'isflash': isflash,
            'scheduleDateTime': scheduleDateTime,
            'period': period
        }
        return await self.makeRequest(self.scheduleUrl, 'AddMultipleSchedule', {**data, **self.get_data()})

    async def send_schedule(self, to, _from, text, isflash, scheduleDateTime, period):
        data = {
            'to': to,
            'from': _from,
            'text': text,
            'isflash': isflash,
            'scheduleDateTime': scheduleDateTime,
            'period': period
        }
        return await self.makeRequest(self.scheduleUrl, 'AddSchedule', {**data, **self.get_data()})

    async def get_schedule_status(self, scheduleId):
        data = {
            'scheduleId': scheduleId
        }
        return await self.makeRequest(self.scheduleUrl, 'GetScheduleStatus', {**data, **self.get_data()})

    async def remove_schedule(self, scheduleId):
        data = {
            'scheduleId': scheduleId
        }
        return await self.makeRequest(self.scheduleUrl, 'RemoveSchedule', {**data, **self.get_data()})

    async def add_usance(self, to, _from, text, isflash, scheduleStartDateTime, repeatAfterDays, scheduleEndDateTime):
        data = {
            'to': to,
            'from': _from,
            'text': text,
            'isflash': isflash,
            'scheduleStartDateTime': scheduleStartDateTime,
            'repeatAfterDays': repeatAfterDays,
            'scheduleEndDateTime': scheduleEndDateTime
        }
        return await self.makeRequest(self.scheduleUrl, 'AddUsance', {**data, **self.get_data()})

    async def add_new_usance(self, to, _from, text, isflash, scheduleStartDateTime, countrepeat, scheduleEndDateTime, periodType):
        data = {
            'to': to,
            'from': _from,
            'text': text,
            'isflash': isflash,
            'scheduleStartDateTime': scheduleStartDateTime,
            'countrepeat': countrepeat,
            'scheduleEndDateTime': scheduleEndDateTime,
            'periodType': periodType
        }
        return await self.makeRequest(self.scheduleUrl, 'AddNewUsance', {**self.get_data(), **data})

    async def add_schedule_send_by_base_number2(self, text, to, bodyId, scheduleDate):
        data = {
            'text': text,
            'to': to,
            'bodyId': bodyId,
            'scheduleDate': scheduleDate
        }
        return await self.makeRequest(self.scheduleUrl, 'AddScheduleSendByBaseNumber2', {**self.get_data(), **data})

    async def get_schedule_details(self, scheduleId):
        return await self.makeRequest(self.scheduleUrl, 'GetScheduleDetails', {**self.get_data(), 'scheduleId': scheduleId})

    async def remove_schedule_list(self, idCollection):
        ids = idCollection if isinstance(idCollection, list) else [idCollection]
        return await self.makeRequest(self.scheduleUrl, 'RemoveScheduleList', {**self.get_data(), 'scheduleIdList':ids})