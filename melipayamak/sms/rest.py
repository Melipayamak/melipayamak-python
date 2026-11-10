import requests


class Rest:
    PATH = "https://rest.payamak-panel.com/api/SendSMS/%s"
    SMART_PATH = "https://rest.payamak-panel.com/api/SmartSMS/%s"
    SHARED_PATH = "https://rest.payamak-panel.com/api/ShareService/%s"
    VOICE_PATH = "https://rest.payamak-panel.com/api/Voice/%s"

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def post(self, url, data):
        r = requests.post(url, data)
        return r.json()

    def get_data(self):
        return {
            'username': self.username,
            'password': self.password
        }

    def send(self, to, _from, text, isFlash=False):
        url = self.PATH % ('SendSMS')
        data = {
            'to': to,
            'from': _from,
            'text': text,
            'isFlash': isFlash
        }
        return self.post(url, {**data, **self.get_data()})

    def send_by_base_number(self, text, to, bodyId):
        url = self.PATH % ('BaseServiceNumber')
        data = {
            'text': text,
            'to': to,
            'bodyId': bodyId
        }
        return self.post(url, {**data, **self.get_data()})
    
    def is_delivered(self, recId):
        url = self.PATH % ('GetDeliveries2')
        data = {
            'recId': recId
        }
        return self.post(url, {**data, **self.get_data()})

    def get_messages(self, location, index, count, _from=''):
        url = self.PATH % ('GetMessages')
        data = {
            'location': location,
            'index': index,
            'count': count,
            'from': _from
        }
        return self.post(url, {**data, **self.get_data()})

    def get_credit(self):
        url = self.PATH % ('GetCredit')
        return self.post(url, self.get_data())

    def get_base_price(self):
        url = self.PATH % ('GetBasePrice')
        return self.post(url, self.get_data())

    def get_numbers(self):
        url = self.PATH % ('GetUserNumbers')
        return self.post(url, self.get_data())

    def send_otp(self, to, _from, code):
        url = self.PATH % ('SendOTP')
        data = {
            'to': to,
            'from': _from,
            'code': code
        }
        return self.post(url, {**self.get_data(), **data})

    def send_multiple_sms(self, _from, to, text):
        url = self.PATH % ('SendMultipleSMS')
        data = {
            'from': _from,
            'to': to,
            'text': text
        }
        return self.post(url, {**self.get_data(), **data})

    def send_schedule(self, text, to, _from, scheduleDate, period):
        url = self.PATH % ('SendSchedule')
        data = {
            'text': text,
            'to': to,
            'from': _from,
            'scheduleDate': scheduleDate,
            'period': period
        }
        return self.post(url, {**self.get_data(), **data})

    def get_schedule(self, scheduleId):
        url = self.PATH % ('GetSchedule')
        return self.post(url, {**self.get_data(), 'scheduleId': scheduleId})

    def get_deliveries(self, recID):
        url = self.PATH % ('GetDeliveries')
        return self.post(url, {**self.get_data(), 'recID': recID})

    def get_new_deliveries(self, recID):
        url = self.PATH % ('GetNewDeliveries')
        return self.post(url, {**self.get_data(), 'recID': recID})

    def get_inbox_count(self):
        url = self.PATH % ('GetInboxCount')
        return self.post(url, self.get_data())

    def get_credit2(self):
        url = self.PATH % ('GetCredit2')
        return self.post(url, self.get_data())
    
    def get_sms_price(self, irancellCount, mciCount, _from, text):
        url = self.PATH % ('GetSmsPrice')
        data = {
            'irancellCount': irancellCount,
            'mciCount': mciCount,
            'from': _from,
            'text': text
        }
        return self.post(url, {**self.get_data(), **data})

    def base_service_number_schedule(self, text, to, bodyId, scheduleDate):
        url = self.PATH % ('BaseServiceNumberSchedule')
        data = {
            text,
            to,
            bodyId,
            scheduleDate
        }
        return self.post(url, {**self.get_data(), **data})

    
    
    
    def send_smart_sms(self, to, text, _from, fromSupportOne, fromSupportTwo):
        url = self.SMART_PATH % ('Send')
        data = {
            'to': to,
            'from': _from,
            'text': text,
            'fromSupportOne': fromSupportOne,
            'fromSupportTwo': fromSupportTwo
        }
        return self.post(url, {**self.get_data(), **data})

    def send_multiple_smart_sms(self, to, text, _from, fromSupportOne, fromSupportTwo):
        url = self.SMART_PATH % ('SendMultiple')
        data = {
            'to': to,
            'from': _from,
            'text': text,
            'fromSupportOne': fromSupportOne,
            'fromSupportTwo': fromSupportTwo
        }
        return self.post(url, {**self.get_data(), **data})

    def get_deliveries_smart_sms(self, id):
        url = self.SMART_PATH % ('GetDeliveries2')
        return self.post(url, {**self.get_data(), 'Id': id})

    def get_deliveries2_smart_sms(self, ids):
        url = self.SMART_PATH % ('GetDeliveries')
        return self.post(url, {**self.get_data(), 'Ids': ids})




    def add_body_shared_service(self, title, body):
        url = self.SHARED_PATH % ('AddBody')
        return self.post(url, {**self.get_data(), 'title': title, 'body': body})

    def edit_body_shared_service(self, bodyId, title, body):
        url = self.SHARED_PATH % ('EditBody')
        return self.post(url, {**self.get_data(), 'bodyId': bodyId, 'title': title, 'body': body})

    def delete_body_shared_service(self, bodyId):
        url = self.SHARED_PATH % ('DeleteBody')
        return self.post(url, {**self.get_data(), 'bodyId': bodyId})

    def get_bodies_shared_service(self, keyword, status):
        url = self.SHARED_PATH % ('GetBodies')
        return self.post(url, {**self.get_data(), 'keyword': keyword, 'status': status})



    def send_speech_text(self, text, to):
        url = self.VOICE_PATH % ('SendSpeechText')
        return self.post(url, {**self.get_data(), 'text': text, 'to': to})

    def send_voice_otp(self, to, code):
        url = self.VOICE_PATH % ('SendVoiceOtp')
        return self.post(url, {**self.get_data(), 'to': to, 'code': code})

    def send_sms_with_speech_text(self, smsBody, speechBody, _from, to):
        url = self.VOICE_PATH % ('SendSMSWithSpeechText')
        data = {
            'smsBody': smsBody,
            'speechBody': speechBody,
            'from': _from,
            'to': to
        }
        return self.post(url, {**self.get_data(), **data})

    def send_sms_with_speech_text_by_schedule_date(self, smsBody, speechBody, _from, to, scheduleDate):
        url = self.VOICE_PATH % ('SendSMSWithSpeechTextBySchduleDate')
        data = {
            'smsBody': smsBody,
            'speechBody': speechBody,
            'from': _from,
            'to': to,
            'scheduleDate': scheduleDate
        }
        return self.post(url, {**self.get_data(), **data})

    def get_send_speech_text_status(self, recId):
        url = self.VOICE_PATH % ('GetSendSpeechTextStatus')
        return self.post(url, {**self.get_data(), 'recId': recId})

    def get_send_speech_text_statuses(self, recIds):
        url = self.VOICE_PATH % ('GetSendSpeechTextStatuses')
        return self.post(url, {**self.get_data, 'recIds': recIds})

    def get_send_sms_with_speech_text_status(self, recId):
        url = self.VOICE_PATH % ('GetSendSMSWithSpeechTextStatus')
        return self.post(url, {**self.get_data(), 'recId': recId})

    def send_bulk_speech_text(self, title, body, receivers, DateToSend, RepeatCount):
        url = self.VOICE_PATH % ('SendBulkSpeechText')
        data = {
            'title': title,
            'body': body,
            'receivers': receivers,
            'DateToSend': DateToSend,
            'RepeatCount': RepeatCount
        }
        return self.post(url, {**self.get_data(), **data})

    def send_bulk_voice_sms(self, title, voiceFileId, receivers, DateToSend, repeatCount):
        url = self.VOICE_PATH % ('SendBulkVoiceSMS')
        data = {
            'title': title,
            'voiceFileId': voiceFileId,
            'receivers': receivers,
            'DateToSend': DateToSend,
            'repeatCount': repeatCount
        }
        return self.post(url, {**self.get_data(), **data})

    def upload_voice_file(self, title, base64StringFile):
        url = self.VOICE_PATH % ('UploadVoiceFile')
        return self.post(url, {**self.get_data(), 'title': title, 'base64StringFile': base64StringFile})

    def upload_voice_file_byte(self, title, file):
        url = self.VOICE_PATH % ('UploadVoiceFileByte')
        return self.post(url, {**self.get_data(), 'title': title, 'file': file})