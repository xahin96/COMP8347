from datetime import timedelta
from datetime import time
from datetime import datetime
from time import strftime

delta = timedelta(
    days=360,
    seconds=0,
    minutes=1,
    hours=5,
)
print(delta)

print('Today is: ', datetime.now())

print('Two years from now it will be: ', datetime.now() + timedelta(days=365*2))

print('In 2 weeks and 3 days it will be: ', datetime.now() + timedelta(weeks=2, days=3))

print('Three weeks ago it was ', (datetime.now() - timedelta(weeks=3)).strftime('%A %B %d, %Y'))


today = datetime.today()
christmas_time = datetime(today.year, 12, 25)
if today > christmas_time:
    print('the number of days left till the next Christmas: ', (datetime(today.year + 1, 12, 25) - today).days)
else:
    print('the number of days left till the next Christmas: ', (christmas_time - today).days)

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

