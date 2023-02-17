from requests import post
from json import dumps
from daemon import Temporal, WeekDay



# Notify the server wether it is within working hours or not

data = dumps({
    "type": "Temporal",
    "event_type": "Hour",
    "event": "NineToFive",
    "context_variable": "worktime",
})

print(post("http://127.0.0.1:5000/daemon", data=data).text)
