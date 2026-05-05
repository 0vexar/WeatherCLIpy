from textual.widgets import Digits
from zoneinfo import ZoneInfo
from timezonefinder import TimezoneFinder
from datetime import datetime
import time

tf = TimezoneFinder()
tz_str = None

def settz(coords:tuple):
    tz_str = tf.timezone_at(lat=coords[0],lng=coords[1])

    if tz_str is None:
        return("Timezone not found")
    else:
        return tz_str


def updateclock(tz_str):
    local_time = datetime.now(ZoneInfo(tz_str))
    local_time_str = local_time.strftime("%I:%M:%S%p")

    return local_time_str

settz((40.046616,-75.428173))

while True:
    time.sleep(1)
    print(updateclock(tz_str))