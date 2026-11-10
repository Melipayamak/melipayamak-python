import aiohttp

class RestAsync:
    PATH = "https://rest.payamak-panel.com/api/SendSMS/%s"
    SMART_PATH = "https://rest.payamak-panel.com/api/SmartSMS/%s"
    SHARED_PATH = "https://rest.payamak-panel.com/api/ShareService/%s"
    VOICE_PATH = "https://rest.payamak-panel.com/api/Voice/%s"

    def __init__(self, username, password):
        self.username = username
        self.password = password

    async def post(self, url, data):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as resp:
                if resp.status == 200:
                    return await resp.text()

    def get_data(self):
        return {
            'username': self.username,
            'password': self.password
        }

    async def send(self, to, _from, text, isFlash=False):
        url = self.PATH % ('SendSMS')
        data = {
            'to': to,
            'from': _from,
            'text': text,
            'isFlash': isFlash
        }
        return await self.post(url, {**data, **self.get_data()})

    async def send_by_base_number(self, text, to, bodyId):
        url = self.PATH % ('BaseServiceNumber')
        data = {
            'text': text,
            'to': to,
            'bodyId': bodyId
        }
        return await self.post(url, {**data, **self.get_data()})
    
    async def is_delivered(self, recId):
        url = self.PATH % ('GetDeliveries2')
        data = {
            'recId': recId
        }
        return await self.post(url, {**data, **self.get_data()})

    async def get_messages(self, location, index, count, _from=''):
        url = self.PATH % ('GetMessages')
        data = {
            'location': location,
            'index': index,
            'count': count,
            'from': _from
        }
        return await self.post(url, {**data, **self.get_data()})

    async def get_credit(self):
        url = self.PATH % ('GetCredit')
        return await self.post(url, self.get_data())

    async def get_base_price(self):
        url = self.PATH % ('GetBasePrice')
        return await self.post(url, self.get_data())

    async def get_numbers(self):
        url = self.PATH % ('GetUserNumbers')
        return await self.post(url, self.get_data())




    async def send_otp(self, to, _from, code):
        url = self.PATH % ('SendOTP')
        data = {
            'to': to,
            'from': _from,
            'code': code
        }
        return await self.post(url, {**self.get_data(), **data})

    async def send_multiple_sms(self, _from, to, text):
        url = self.PATH % ('SendMultipleSMS')
        data = {
            'from': _from,
            'to': to,
            'text': text
        }
        return await self.post(url, {**self.get_data(), **data})

    async def send_schedule(self, text, to, _from, scheduleDate, period):
        url = self.PATH % ('SendSchedule')
        data = {
            'text': text,
            'to': to,
            'from': _from,
            'scheduleDate': scheduleDate,
            'period': period
        }
        return await self.post(url, {**self.get_data(), **data})

    async def get_schedule(self, scheduleId):
        url = self.PATH % ('GetSchedule')
        return await self.post(url, {**self.get_data(), 'scheduleId': scheduleId})

    async def get_deliveries(self, recID):
        url = self.PATH % ('GetDeliveries')
        return await self.post(url, {**self.get_data(), 'recID': recID})

    async def get_new_deliveries(self, recID):
        url = self.PATH % ('GetNewDeliveries')
        return await self.post(url, {**self.get_data(), 'recID': recID})

    async def get_inbox_count(self):
        url = self.PATH % ('GetInboxCount')
        return await self.post(url, self.get_data())

    async def get_credit2(self):
        url = self.PATH % ('GetCredit2')
        return await self.post(url, self.get_data())
    
    async def get_sms_price(self, irancellCount, mciCount, _from, text):
        url = self.PATH % ('GetSmsPrice')
        data = {
            'irancellCount': irancellCount,
            'mciCount': mciCount,
            'from': _from,
            'text': text
        }
        return await self.post(url, {**self.get_data(), **data})

    async def base_service_number_schedule(self, text, to, bodyId, scheduleDate):
        url = self.PATH % ('BaseServiceNumberSchedule')
        data = {
            text,
            to,
            bodyId,
            scheduleDate
        }
        return await self.post(url, {**self.get_data(), **data})

    
    
    
    async def send_smart_sms(self, to, text, _from, fromSupportOne, fromSupportTwo):
        url = self.SMART_PATH % ('Send')
        data = {
            'to': to,
            'from': _from,
            'text': text,
            'fromSupportOne': fromSupportOne,
            'fromSupportTwo': fromSupportTwo
        }
        return await self.post(url, {**self.get_data(), **data})

    async def send_multiple_smart_sms(self, to, text, _from, fromSupportOne, fromSupportTwo):
        url = self.SMART_PATH % ('SendMultiple')
        data = {
            'to': to,
            'from': _from,
            'text': text,
            'fromSupportOne': fromSupportOne,
            'fromSupportTwo': fromSupportTwo
        }
        return await self.post(url, {**self.get_data(), **data})

    async def get_deliveries_smart_sms(self, id):
        url = self.SMART_PATH % ('GetDeliveries2')
        return await self.post(url, {**self.get_data(), 'Id': id})

    async def get_deliveries2_smart_sms(self, ids):
        url = self.SMART_PATH % ('GetDeliveries')
        return await self.post(url, {**self.get_data(), 'Ids': ids})




    async def add_body_shared_service(self, title, body):
        url = self.SHARED_PATH % ('AddBody')
        return await self.post(url, {**self.get_data(), 'title': title, 'body': body})

    async def edit_body_shared_service(self, bodyId, title, body):
        url = self.SHARED_PATH % ('EditBody')
        return await self.post(url, {**self.get_data(), 'bodyId': bodyId, 'title': title, 'body': body})

    async def delete_body_shared_service(self, bodyId):
        url = self.SHARED_PATH % ('DeleteBody')
        return await self.post(url, {**self.get_data(), 'bodyId': bodyId})

    async def get_bodies_shared_service(self, keyword, status):
        url = self.SHARED_PATH % ('GetBodies')
        return await self.post(url, {**self.get_data(), 'keyword': keyword, 'status': status})



    async def send_speech_text(self, text, to):
        url = self.VOICE_PATH % ('SendSpeechText')
        return await self.post(url, {**self.get_data(), 'text': text, 'to': to})

    async def send_voice_otp(self, to, code):
        url = self.VOICE_PATH % ('SendVoiceOtp')
        return await self.post(url, {**self.get_data(), 'to': to, 'code': code})

    async def send_sms_with_speech_text(self, smsBody, speechBody, _from, to):
        url = self.VOICE_PATH % ('SendSMSWithSpeechText')
        data = {
            'smsBody': smsBody,
            'speechBody': speechBody,
            'from': _from,
            'to': to
        }
        return await self.post(url, {**self.get_data(), **data})

    async def send_sms_with_speech_text_by_schedule_date(self, smsBody, speechBody, _from, to, scheduleDate):
        url = self.VOICE_PATH % ('SendSMSWithSpeechTextBySchduleDate')
        data = {
            'smsBody': smsBody,
            'speechBody': speechBody,
            'from': _from,
            'to': to,
            'scheduleDate': scheduleDate
        }
        return await self.post(url, {**self.get_data(), **data})

    async def get_send_speech_text_status(self, recId):
        url = self.VOICE_PATH % ('GetSendSpeechTextStatus')
        return await self.post(url, {**self.get_data(), 'recId': recId})

    async def get_send_speech_text_statuses(self, recIds):
        url = self.VOICE_PATH % ('GetSendSpeechTextStatuses')
        return await self.post(url, {**self.get_data, 'recIds': recIds})

    async def get_send_sms_with_speech_text_status(self, recId):
        url = self.VOICE_PATH % ('GetSendSMSWithSpeechTextStatus')
        return await self.post(url, {**self.get_data(), 'recId': recId})

    async def send_bulk_speech_text(self, title, body, receivers, DateToSend, RepeatCount):
        url = self.VOICE_PATH % ('SendBulkSpeechText')
        data = {
            'title': title,
            'body': body,
            'receivers': receivers,
            'DateToSend': DateToSend,
            'RepeatCount': RepeatCount
        }
        return await self.post(url, {**self.get_data(), **data})

    async def send_bulk_voice_sms(self, title, voiceFileId, receivers, DateToSend, repeatCount):
        url = self.VOICE_PATH % ('SendBulkVoiceSMS')
        data = {
            'title': title,
            'voiceFileId': voiceFileId,
            'receivers': receivers,
            'DateToSend': DateToSend,
            'repeatCount': repeatCount
        }
        return await self.post(url, {**self.get_data(), **data})

    async def upload_voice_file(self, title, base64StringFile):
        url = self.VOICE_PATH % ('UploadVoiceFile')
        return await self.post(url, {**self.get_data(), 'title': title, 'base64StringFile': base64StringFile})

    async def upload_voice_file_byte(self, title, file):
        url = self.VOICE_PATH % ('UploadVoiceFileByte')
        return await self.post(url, {**self.get_data(), 'title': title, 'file': file})
