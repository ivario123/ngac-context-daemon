# Context notify

Provides a clean and simple way of creating daemons that notify the NGAC sever when that daemon's context has changed.

## Daemon types

Currently, the system only provides temporal daemons i.e. daemons that notify after a certain time.

## Setting up the system

Note that this repo depends on the NgacApi module in the [NGAC_ABE](https://github.com/ivario123/NGAC_ABE) repository. Install that repo first.


1. Change NGAC URL to the correct one in `event.py`
2. Install daemonizer `pip install ./daemonizer`
3. Run the app `python src`

## Currently supported daemons

### Temporal

- WeekDay
  - DayOfTheWeek, literal
  - WorkDay, true or false
- Hour
  - NineToFive, true or false
  - SixToEighteen, true or false

## Example usage

```python
from requests import post
from json import dumps


# Notify the server wether it's a workday or not

data = dumps(
    {
        "type": "Temporal",
        "event_type": "WeekDay",
        "event": "WorkDay",
        "context_variable": "weekday",
    }
)

print(post("http://127.0.0.1:5001/daemon", data=data).text)
```
