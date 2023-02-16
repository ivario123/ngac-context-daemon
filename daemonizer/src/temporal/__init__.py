from event import *
from typing import Type
from .wait import wait_until, datetime, first
from time import time, sleep
from NgacApi.ngac import NGAC
from result import unwrap


class WeekDay(EventGroup):
    """
    Reports on weekday to the server
    """
    class Change(Event):
        """
        Triggers on day change
        """
        started = False

        def get_next_delay(self):
            if not self.started:
                self.started = True
                return
            wait_until(first(("00:01",)))
        days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Sunday"
        ]

        def trigger(self):
            # Print the current weekday
            # Not quite sure if we should have a second one that detects workday/weekend or not.
            print(super().NGAC.change_context(
                [f"weekday:{str(datetime.weekday(datetime.now())<6).lower()}"], token="epp_token"))
            print(self.days[datetime.weekday(datetime.now())])

    mapping: dict[str, Type[Event]] = {
        "Change": Change
    }


class Second(EventGroup):
    """
    Reports on seconds to the server
    """
    class Change(Event):
        """
        Triggers on second change
        """

        def get_next_delay(self):
            sleep(1)

        def trigger(self):
            print("Second changed")

    mapping: dict[str, Type[Event]] = {
        "Change": Change
    }
