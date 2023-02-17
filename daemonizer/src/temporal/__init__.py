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
    class DayOfTheWeek(Event):
        """
        Triggers on day change
        """
        started = False

        def get_next_delay(self):
            if not self.started:
                self.started = True
                return
            wait_until(first(("00:00",)))
        days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"
            "Sunday"
        ]

        def trigger(self, context_variable: str):
            print(super().NGAC.change_context(
                [f"{context_variable}:{self.days[datetime.weekday(datetime.now())]}"], token="epp_token"))
            print(self.days[datetime.weekday(datetime.now())])

    class WorkDay(Event):
        """
        Triggers on day change
        """
        started = False

        def get_next_delay(self):
            if not self.started:
                self.started = True
                return
            wait_until(first(("00:00",)))

        def trigger(self, context_variable: str):
            print(super().NGAC.change_context(
                [f"{context_variable}:{str(datetime.weekday(datetime.now())<6).lower()}"], token="epp_token"))

    mapping: dict[str, Type[Event]] = {
        "DayOfTheWeek": DayOfTheWeek,
        "WorkDay": WorkDay
    }


class Hour(EventGroup):
    """
    Reports on hours to the server
    """
    class NineToFive(Event):
        """
        Reports wether the time is between nine and five
        """
        started = False
        state = "false"

        def valid(self):
            now = datetime.now()
            self.state = f"{(now.hour > 9 and now.hour < 17)}".lower()

        def get_next_delay(self):
            if not self.started:
                self.started = True
                return
            wait_until(first(["09:00", "17:00"]))

        def trigger(self, context_variable: str):
            self.valid()
            print(f"{context_variable}:{self.state}")
            print(super().NGAC.change_context(
                [f"{context_variable}:{self.state}"], token="epp_token"))

    class SixToEighteen(Event):
        """
        Reports wether the time is between six and eighteen
        """
        started = False
        state = False

        def valid(self):
            now = datetime.now()
            self.state = now.hour > 6 and now.hour < 18

        def get_next_delay(self):
            if not self.started:
                self.started = True
                return
            wait_until(first(["06:00", "18:00"]))

        def trigger(self, context_variable: str):
            self.valid()
            print()
            print(super().NGAC.change_context(
                [f"{context_variable}:{self.state}"], token="epp_token"))

    mapping: dict[str, Type[Event]] = {
        "NineToFive": NineToFive,
        "SixToEighteen": SixToEighteen
    }
