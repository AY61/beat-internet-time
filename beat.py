import datetime
import pytz
import math

def get_beat_time():

    tz = pytz.timezone("Europe/Zurich")
    current_time = datetime.datetime.now(tz)

    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second
    microsecond = current_time.microsecond

    total_seconds = (hour*3600) + (minute*60) + second + (microsecond/1000000)
    beats = round(total_seconds / 86.4, 2)
    beats_string = 0
    
    if beats < 10:
        beats_string = "@00" + str(beats)
    elif beats < 100:
        beats_string = "@0" + str(beats)
    else:
        beats_string = "@" + str(beats)

    return beats_string