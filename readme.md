# Melipayamak Python


<div dir='rtl'>

### معرفی وب سرویس ملی پیامک
ملی پیامک یک وب سرویس کامل برای ارسال و دریافت پیامک و پیامک صوتی و مدیریت کامل خدمات دیگر است که براحتی میتوانید از آن استفاده کنید.

<hr>

### نصب

<p>قبل از نصب نیاز به ثبت نام در سایت ملی پیامک دارید.</p>

[**ثبت نام به همراه دریافت 200 پیامک هدیه جهت تست وبسرویس**](http://www.melipayamak.com/)

<p>پس ازثبت نام  برای نصب از راههای زیر میتوانید اقدام کنید.</p>

#### پیشنیاز ها

برای استفاده از نمونه کدهای پایتون نیاز به نصب پکیج های زیر است:

</div>


```
pip install zeep
pip install requests

//following for async
pip install aiohttp
pip install asyncio
```


<div dir='rtl'>

سپس repository را دانلود کنید

	
	
#### نحوه استفاده
نمونه کد برای ارسال پیامک



</div>



```py
from melipayamak import Api
username = 'username'
password = 'password'
api = Api(username,password)
sms = api.sms()
to = '09123456789'
_from = '5000...'
text = 'تست وب سرویس ملی پیامک'
response = sms.send(to,_from,text)
print(response)

```


<div dir='rtl'>

از آنجا که وب سرویس ملی پیامک تنها محدود به ارسال پیامک نیست  شما از طریق  زیر میتوانید به وب سرویس ها دسترسی کامل داشته باشید:


</div>

```py
// وب سرویس پیامک
sms_rest = api.sms()
sms_soap = api.sms('soap')
// وب سرویس تیکت پشتیبانی
ticket = api.ticket()
// وب سرویس برای مدیریت کامل  ارسال انبوه پیامک
branch = api.branch()
//وب سرویس کاربران
users = api.users()
//وب سرویس دفترچه تلفن
contacts = api.contacts()

```

<div dir='rtl'>

##### حالت آسنکرون
برای استفاده از وب سرویس در حالت آسنکرون به صورت زیر اقدام کنید. اطلاعات بیشتر در قالب نمونه پروژه تهیه شده است.
</div>

```php
// وب سرویس پیامک
$smsRestAsync = $api->sms('rest', 'async');
$smsSoapAsync = $api->sms('soap', 'async');
// وب سرویس تیکت پشتیبانی
$ticket = $api->ticketAsync();
// وب سرویس برای مدیریت کامل  ارسال انبوه پیامک
$branch = $api->branchAsync();
//وب سرویس کاربران
$users = $api->usersAsync();
//وب سرویس دفترچه تلفن
$contacts = $api->contactsAsync();
```

<div dir='rtl'>


#### تفاوت های وب سرویس پیامک rest و soap
از آنجا که ملی پیامک وب سرویس کاملی رو در اختیار توسعه دهندگان میگزارد برای راحتی کار با وب سرویس پیامک علاوه بر وب سرویس اصلی soap وب سرویس rest رو هم در اختیار توسعه دهندگان گزاشته شده تا راحتتر بتوانند با وب سرویس کار کنند. تفاوت اصلی این دو در تعداد متد هاییست که میتوانید با آن کار کنید. برای کار های پایه میتوان از وب سرویس rest استفاده کرد برای دسترسی بیشتر و استفاده پیشرفته تر نیز باید از وب سرویس باید از وب سرویس soap استفاده کرد.
جهت  مطالعه بیشتر وب سرویس ها به قسمت وب سرویس پنل خود مراجعه کنید.
<hr/>

###  اطلاعات بیشتر

برای مطالعه بیشتر و دریافت راهنمای وب سرویس ها و آشنایی با پارامتر های ورودی و خروجی وب سرویس به صفحه معرفی
[وب سرویس ملی پیامک](https://github.com/Melipayamak/Webservices)
مراجعه نمایید .


<hr/>


### وب سرویس پیامک

متد های وب سرویس:


</div>

#### ارسال

```py
sms_rest.send(to,from,text,is_flash)
sms_soap.send(to,from,text,is_flash)
```
* در وب سرویس soap به جای ارسال یک شماره آرایه ای از شماره ها نیز قابل قبول است

#### ارسال از خط خدماتی اشتراکی

```py
sms_rest.send_by_base_number(text, to, bodyId)
sms_soap.send_by_base_number(text, to, bodyId)
```

#### دریافت وضعیت ارسال
```py
sms_rest.is_delivered(recId)
sms_soap.is_delivered(recId)
```
* به در وب سرویس soap به جای تک آیدی میتوان آرایه نیز ارسال کرد.
#### لیست پیامک ها
```py
sms_rest.get_messages(location,index,count,from)
sms_soap.get_messages(location,index,count,from)
sms_soap.get_messages_str(location,index,count,from)
// جهت دریافت به صورت رشته ای
sms_soap.get_messages_by_date(location,index,count,from,date_from,date_to)
//جهت دریافت بر اساس تاریخ
sms_soap.get_users_messages_by_date(location,index,count,from,date_from,date_to)
// جهت دریافت پیام های کاربران بر اساس تاریخ 
```

#### موجودی


```py
sms_rest.get_credit()
sms_soap.get_credit()
```

#### تعرفه پایه / دریافت قیمت قبل از ارسال
```py
sms_rest.get_base_price
sms_soap.get_price(irancell_count,mtn_count,from,text)
```
#### لیست شماره اختصاصی
```py
sms_rest.get_numbers()
```

#### بررسی تعداد پیامک های دریافتی
```py
sms_soap.get_inbox_count(is_read)
//پیش فرض خوانده نشده 
```

#### ارسال پیامک پیشرفته
```py
sms_soap.send2(to,from,text,is_flash,udh)
```

#### مشاهده مشخصات پیام
```py
sms_soap.get_messages_receptions(msgId,from_rows)
```


#### حذف پیام دریافتی
```py
sms_soap.remove(msgIds)
```


#### ارسال زماندار
```py
sms_soap.send_schedule(to,from,text,is_flash,schedule_dateTime,period)
```

#### ارسال زماندار متناظر
```py
sms_soap.send_multiple_schedule(to,from,text,is_flash,schedule_dateTime,period)
```


#### ارسال سررسید
```py
sms_soap.add_usance(to,from,text,isflash,schedule_start_date_time,repeat_after_days,schedule_end_dateTime)
```

#### مشاهده وضعیت ارسال زماندار
```py
sms_soap.get_schedule_status(schId)
```

#### حذف پیامک زماندار
```py
sms_soap.remove_schedule(schId)
```

### وب سرویس پیامک صوتی

####  ارسال پیامک همراه با تماس صوتی
```py
sms_soap.send_with_speech(to,from,text,speech)
```

####  ارسال پیامک همراه با تماس صوتی به صورت زمانبندی
```py
sms_soap.send_with_speech_schdule_date(to,from,text,speech,schedule_date)
```

####  دریافت وضعیت پیامک همراه با تماس صوتی 
```py
sms_soap.get_send_with_speech(rec_id)
```

#### تماس انبوه زماندار
```py
sms_soap.send_bulk_speech_text(self, title, body, receivers, DateToSend, repeatCount)
```

#### تماس انبوه زماندار با انتخاب فایل
```py
sms_soap.send_bulk_voice_sms(self, title, voiceFileId, receivers, DateToSend, repeatCount)
```

#### آپلود فایل صوتی
```py
sms_soap.upload_voice_file(self, title, base64StringFile)
```

### وب سرویس ارسال انبوه/منطقه ای

#### دریافت شناسه شاخه های بانک شماره
```py
branch.get(owner)
```


#### اضافه کردن یک بانک شماره جدید
```py
branch.add(branch_name,owner)
```

#### اضافه کردن شماره به بانک
```py
branch.add_number(mobile_numbers,branch_id)
```

#### حذف یک بانک
```py
branch.remove(branch_id)
```

#### ارسال انبوه از طریق بانک
```py
branch.send_bulk(from,title,message,branch,Date_to_send,request_count,bulk_type,row_from,range_from,range_to)
branch.send_bulk2(from,title,message,branch,Date_to_send,request_count,bulk_type,row_from,range_from,range_to)
```

#### تعداد شماره های موجود
```py
branch.get_bulk_count(branch,range_from,range_to)
```

#### گزارش گیری از ارسال انبوه
```py
branch.get_bulk_receptions(bulk_id,from_rows)
```


#### تعیین وضعیت ارسال 
```py
branch.get_bulk_status(bulk_id)
```

#### تعداد ارسال های امروز
```py
branch.get_today_sent()
```

#### تعداد ارسال های کل

```py
branch.get_total_sent()
```

#### حذف ارسال منطقه ای
```py
branch.remove_bulk(id)
```

#### ارسال متناظر
```py
branch.send_multiple_sms(to,from,text,is_flash,udh)
```

#### نمایش دهنده وضعیت گزارش گیری

```py
branch.update_bulk_delivery(bulk_id)
```
### وب سرویس تیکت

#### ثبت تیکت جدید
```py
ticket.add(title,content,alert_with_sms)
```

#### جستجو و دریافت تیکت ها

```py
ticket.get_received(ticket_owner,ticket_type,keyword)
```

#### دریافت تعداد تیکت های کاربران
```py
ticket.get_received_count(ticket_type)
```

#### دریافت تیکت های ارسال شده
```py
ticket.get_sent(ticket_owner,ticket_type,keyword)
```

#### دریافت تعداد تیکت های ارسال شده
```py
ticket.get_sent_count(ticket_type)
```


#### پاسخگویی به تیکت
```py
ticket.response(ticket_id,type,content,alert_with_sms)
```

### وب سرویس دفترچه تلفن

#### اضافه کردن گروه جدید
```py
contacts.add_group(group_name,Descriptions,show_to_childs)
```

#### اضافه کردن کاربر جدید
```py
contacts.add(options)

```

#### بررسی موجود بودن شماره در دفترچه تلفن
```py
contacts.check_mobile_exist(mobile_number)
```

#### دریافت اطلاعات دفترچه تلفن
```py
contacts.get(group_id,keyword,from,count)
```
#### دریافت گروه ها
```py
contacts.get_groups()
```
#### ویرایش مخاطب
```py
contacts.change(options)
```

#### حذف مخاطب
```py
contacts.remove(mobile_number)
```
#### دریافت اطلاعات مناسبت های فرد
```py
contacts.get_events(contact_id)
```



### وب سرویس کاربران

#### ثبت فیش واریزی
```py
users.add_payment(options)
```

#### اضافه کردن کاربر جدید در سامانه
```py
users.add(options)

```

#### اضافه کردن کاربر جدید در سامانه(کامل)
```py
users.add_complete(options)
```

#### اضافه کردن کاربر جدید در سامانه(WithLocation)
```py
users.add_with_location(options)
```
#### بدست آوردن ID کاربر
```py
users.authenticate()
```
#### تغییر اعتبار
```py
users.change_credit(amount,description,target_username,Get_tax)
```

#### فراموشی رمز عبور
```py
users.forgot_password(mobile_number,email_address,target_username)
```
#### دریافت تعرفه پایه کاربر
```py
users.get_base_price(target_username)
```

#### دریافت اعتبار کاربر
```py
users.get_credit(target_username)
```

#### دریافت مشخصات کاربر
```py
users.get_details(target_username)
```

#### دریافت شماره های کاربر
```py
users.get_numbers()
```

#### دریافت تراکنش های کاربر
```py
users.get_transactions(target_username,credit_type,date_from,date_to,keyword)
```

#### دریافت اطلاعات  کاربران
```py
users.get()
```


#### دریافت اطلاعات  فیلترینگ
```py
users.has_filter(text)
```


####  حذف کاربر
```py
users.remove(target_username)
```


#### مشاهده استان ها
```py
users.get_provinces()
```

#### مشاهده کد شهرستان 
```py
users.get_cities(province_id)
```


#### مشاهده تاریخ انقضای کاربر 
```py
users.get_expire_date()
```

