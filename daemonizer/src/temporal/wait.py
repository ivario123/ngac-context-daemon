"""
Waits until the desired time.

This assumes that the time zone is consistent between the target time and the current time
"""
from datetime import datetime, timedelta
from time import sleep
from dateutil import parser


def first(times: list[str]) -> datetime:
    ret: list[datetime] = []
    for time in times:
        t: datetime = parser.parse( time)
        if t > datetime.now():
            ret.append(t)
        else:
            ret.append(t+timedelta(days=1))
    print(ret)
    return min(ret)


def wait_until(target: datetime):
    now: datetime = datetime.now()
    delta: timedelta = target-now
    if delta.seconds <= 0:
        raise Exception("The requested target is in the past")
    print(f"Waiting until {target}")
    sleep(delta.seconds)
