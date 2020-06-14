import datetime

print(f'{"#"*50}')
now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%d/%m/%Y'))
print(f'{"#"*50}')
t = datetime.time(hour=10, minute=10, second=10, microsecond=10)
print(t)
print(t.isoformat())
print(t.strftime('%H_%M_%S_%f'))
print(f'{"#"*50}')
print(now)
d = datetime.timedelta(weeks=10)
d = datetime.timedelta(days=10)
d = datetime.timedelta(hours=10)
d = datetime.timedelta(minutes=1000)
d = datetime.timedelta(seconds=100000000)
print(now-d)

import time
print(f'{"#"*50}')
time.sleep(2)
print(time.time()) # epoch-time
print(f'{"#"*50}')

