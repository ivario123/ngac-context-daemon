from threading import Thread, Lock
from temporal import WeekDay, Hour
from event import EventGroup, Event
from typing import Type
from time import sleep


class Daemonizer:
    """
    Keeps a list of all daemon threads
    """
    mutex = Lock()

    def __init__(self) -> None:
        self.daemons: list[Daemon] = []

    def __add__(self, other: "Daemon") -> None:
        if not issubclass(type(other), Daemon):
            raise Exception("Incorrect type")
        self.daemons.append(other)


class Daemon:
    """
    A marker class for all types of daemons
    """
    mapping: dict[str, Type[EventGroup]] = {}
    """
    String mapping to every possible event group for the daemon type
    """

    def __init__(self, event_type: Type[EventGroup], event: Type[Event]):
        """
        Creates a new daemon that listens for the event.

        When the event occurs it will notify the NGAC server
        """
        pass

    def body(self):
        """
        This is the main part of the daemon.

        This function will run as a thread, allowing the program to run asynchronously from 
        the main program acting like a daemon.
        """
        pass


class Temporal(Daemon):
    """
    A daemon that triggers on time based events
    """
    mapping: dict[str, Type[EventGroup]] = {
        "WeekDay": WeekDay,
        "Hour": Hour,
    }
    # This daemon is entirely self contained to this module

    def __init__(self, event_type: Type[EventGroup], event: Type[Event], context_variable: str):
        self.event = event_type(event)
        self.context_variable = context_variable
        self.thread = Thread(
            target=self.body, name="Temporal body")
        self.thread.start()

    def body(self):
        # Do stuff here
        print(self.event.event.trigger(self.context_variable))
        self.event.event.get_next_delay()

        self.thread.run()


mapping: dict[str, Type[Daemon]] = {
    "Temporal": Temporal
}
