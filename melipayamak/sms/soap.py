from zeep import Client


class Soap:
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

    def get_credit(self):
        client = Client(self.sendUrl)
        result = client.service.GetCredit(**self.get_data())
        return result

    def is_delivered(self, recId):
        client = Client(self.sendUrl)
        result = None
        
        if isinstance(recId, list):
            data = {
                'recIds': recId
            }
            result = client.service.GetDeliveries(**self.get_data(), **data)
        else:
            data = {
                'recId': recId
            }
            result = client.service.GetDelivery(**data)
        return result

    def send(self, to, _from, text, isflash=False):
        client = Client(self.sendUrl)
        data = {
            'from': _from,
            'text': text,
            'isflash': isflash,
            'to': to
        }
        result = None
        if isinstance(to, list):
            result = client.service.SendSimpleSMS(**self.get_data(), **data)
        else:
            result = client.service.SendSimpleSMS2(**self.get_data(), **data)
        return result

    def send2(self, to, _from, text, isflash=False, udh=''):
        client = Client(self.sendUrl)
        to = to if isinstance(to, list) else [to]
        data = {
            'from': _from,
            'text': text,
            'isflash': isflash,
            'to': to,
            'udh': udh
        }
        result = client.service.SendSms(**self.get_data(), **data)
        return result

    def send_with_domain(self, to, _from, text, isflash, domainName):
        client = Client(self.sendUrl)
        data = {
            'from': _from,
            'text': text,
            'isflash': isflash,
            'to': to,
            'domainName': domainName
        }
        result = client.service.SendWithDomain(**self.get_data(), **data)
        return result

    def send_by_base_number(self, text, to, bodyId):
        client = Client(self.sendUrl)
        data = {
            'text': text,
            'to': to,
            'bodyId': bodyId
        }
        result = None
        if isinstance(text, list):
            result = client.service.SendByBaseNumber(**self.get_data(), **data)
        else:
            result = client.service.SendByBaseNumber2(**self.get_data(), **data)
        return result
    
    def get_messages(self, location, index, count, _from=''):
        client = Client(self.sendUrl)
        data = {
            'location': location,
            'index': index,
            'count': count,
            'from': _from
        }
        result = client.service.getMessages(**self.get_data(), **data)
        return result

    def get_messages_str(self, location, index, count, _from=''):
        client = Client(self.receiveUrl)
        data = {
            'location': location,
            'index': index,
            'count': count,
            'from': _from
        }
        result = client.service.GetMessageStr(**self.get_data(), **data)
        return result

    def get_messages_by_date(self, location, index, count, dateFrom, dateTo, _from=''):
        client = Client(self.receiveUrl)
        data = {
            'location': location,
            'index': index,
            'count': count,
            'from': _from,
            'dateFrom': dateFrom,
            'dateTo': dateTo
        }
        result = client.service.GetMessagesByDate(**self.get_data(), **data)
        return result

    def get_messages_receptions(self, msgId, fromRows):
        client = Client(self.receiveUrl)
        data = {
            'msgId': msgId,
            'fromRows': fromRows
        }
        result = client.service.GetMessagesReceptions(**self.get_data(), **data)
        return result

    def get_users_messages_by_date(self, location, index, count, _from,dateFrom, dateTo):
        client = Client(self.receiveUrl)
        data = {
            'location': location,
            'index': index,
            'count': count,
            'from': _from,
            'dateFrom': dateFrom,
            'dateTo': dateTo
        }
        result = client.service.GetUsersMessagesByDate(
            **self.get_data(), **data)
        return result

    def remove(self, msgIds):
        client = Client(self.receiveUrl)
        data = {
            'msgIds': msgIds,
        }
        result = client.service.RemoveMessages2(**self.get_data(), **data)
        return result

    def get_price(self, irancellCount, mtnCount,  _from, text):
        client = Client(self.sendUrl)
        data = {
            'irancellCount': irancellCount,
            'mtnCount': mtnCount,
            'text': text,
            'from': _from
        }
        result = client.service.GetSmsPrice(**self.get_data(), **data)
        return result

    def get_inbox_count(self, isRead=False):
        client = Client(self.sendUrl)
        data = {
            'isRead': isRead,
        }
        result = client.service.GetInboxCount(**self.get_data(), **data)
        return result

    def send_with_speech(self, to, _from, text, speech):
        client = Client(self.voiceUrl)
        data = {
            'to': to,
            'from': _from,
            'smsBody': text,
            'speechBody': speech
        }
        result = client.service.SendSMSWithSpeechText(**self.get_data(), **data)
        return result

    def send_with_speech_schdule_date(self, to, _from, text, speech, scheduleDate):
        client = Client(self.voiceUrl)
        data = {
            'to': to,
            'from': _from,
            'smsBody': text,
            'speechBody': speech,
            'scheduleDate': scheduleDate
        }
        result = client.service.SendSMSWithSpeechTextBySchduleDate(
            **self.get_data(), **data)
        return result

    def get_send_with_speech(self, recId):
        client = Client(self.voiceUrl)
        data = {
            'recId': recId
        }
        result = client.service.GetSendSMSWithSpeechTextStatus(
            **self.get_data(), **data)
        return result

    def get_multi_delivery(self, recId):
        client = Client(self.sendUrl)
        data = {
            'recId': recId
        }
        result = client.service.GetMultiDelivery2(**self.get_data(), **data)
        return result

    def send_multiple_schedule(self, to, _from, text, isflash, scheduleDateTime, period):
        client = Client(self.scheduleUrl)
        data = {
            'to': to,
            'from': _from,
            'text': text,
            'isflash': isflash,
            'scheduleDateTime': scheduleDateTime,
            'period': period
        }
        result = client.service.AddMultipleSchedule(**self.get_data(), **data)
        return result

    def send_schedule(self, to, _from, text, isflash, scheduleDateTime, period):
        client = Client(self.scheduleUrl)
        data = {
            'to': to,
            'from': _from,
            'text': text,
            'isflash': isflash,
            'scheduleDateTime': scheduleDateTime,
            'period': period
        }
        result = client.service.AddSchedule(**self.get_data(), **data)
        return result

    def get_schedule_status(self, scheduleId):
        client = Client(self.scheduleUrl)
        data = {
            'scheduleId': scheduleId
        }
        result = client.service.GetScheduleStatus(**self.get_data(), **data)
        return result

    def remove_schedule(self, scheduleId):
        client = Client(self.scheduleUrl)
        data = {
            'scheduleId': scheduleId
        }
        result = client.service.RemoveSchedule(**self.get_data(), **data)
        return result

    def add_usance(self, to, _from, text, isflash, scheduleStartDateTime, repeatAfterDays, scheduleEndDateTime):
        client = Client(self.scheduleUrl)
        data = {
            'to': to,
            'from': _from,
            'text': text,
            'isflash': isflash,
            'scheduleStartDateTime': scheduleStartDateTime,
            'repeatAfterDays': repeatAfterDays,
            'scheduleEndDateTime': scheduleEndDateTime
        }
        result = client.service.AddUsance(**self.get_data(), **data)
        return result
