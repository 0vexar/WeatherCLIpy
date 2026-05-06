from textual.widgets import Digits
from zoneinfo import ZoneInfo
from timezonefinder import TimezoneFinder
from datetime import datetime
import time

tf = TimezoneFinder()

def get_timezone(coords:tuple):
    tz_str = tf.timezone_at(lat=coords[0],lng=coords[1])

    if tz_str is None:
        return None
    else:
        return tz_str

def get_time(tz_str):
    
    __local_time__ = datetime.now(ZoneInfo(tz_str))
    
    return __local_time__.strftime("%I:%M:%S%p")