import requests
import config
import json
from datetime import datetime
from pytz import timezone
import pytz
from dateutil import tz
from config import APIKEY

baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {'q': 'Santa Clara, CA, US', 'appid': APIKEY, 'cnt':'1', 'units':'imperial'}
response = requests.get(baseUrl, params=parameters)

content = response.content

info = json.loads(content)

cityInfo = info['city']

from_zone = tz.gettz('UTC')
to_zone = tz.tzlocal()

# Convert date unix utc string to int
sunrise = int((cityInfo['sunrise']))
# Use unix int timestamp to print UTC
sun = datetime.utcfromtimestamp(sunrise)
# sun is a naive datetime object. Make it aware and UTC
sun_utc = sun.replace(tzinfo=from_zone)
# use aware sun object to generate local time zone sunrise time
rise = sun_utc.astimezone(to_zone)
# Print sunrise in LT
print(rise.strftime('%Y-%m-%d %H:%M:%S'))
