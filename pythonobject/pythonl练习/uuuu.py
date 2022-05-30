import datetime

now = datetime.datetime.now()
print(str(now.hour+now.minute+now.second) + datetime.datetime.now().strftime('%Y%m%d'))
