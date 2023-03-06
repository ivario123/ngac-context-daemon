# Context notify

Provides a clean and simple way of creating daemons that notify the NGAC sever when that daemon's context has changed.

## Daemon types

Currently, the system only provides temporal daemons i.e. daemons that notify after a certain time.

## Setting up the system

1. Install dependencies
2. Change NGAC url to the correct one in `event.py`
3. Install daemonizer `pip install ./daemonizer`
4. Run the app `python src`
