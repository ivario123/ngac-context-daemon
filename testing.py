from requests import post
from json import dumps
from daemon import Temporal, WeekDay


data = dumps({
    "type": "Temporal",
    "event_type": "WeekDay",
    "event": "Change",
    "context_variable": "weekday",
})

print(post("http://127.0.0.1:5000/daemon", data=data).text)
