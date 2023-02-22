from requests import post
from json import dumps


# Notify the server wether it is within working hours or not

data = dumps(
    {
        "type": "Temporal",
        "event_type": "WeekDay",
        "event": "WorkDay",
        "context_variable": "weekday",
    }
)

print(post("http://127.0.0.1:5000/daemon", data=data).text)
