from flask import Flask, request, url_for
from threading import Lock
from require import fields
from daemon import *

daemon_mutex = Lock()

app = Flask(__name__)


@app.route("/")
def index():
    return "index"


@app.route("/daemon_types", methods=["POST"])
def daemon_types():
    return ",".join(mapping.keys())


@app.route("/event_types", methods=["POST"])
@fields(request)
def event_types(type: str):

    type: Type[Daemon] = mapping.get(type, None)
    if not type:
        return "No such daemon type", 400
    return ",".join(type.mapping.keys())


@app.route("/event_types", methods=["POST"])
@fields(request)
def event_types(type: str, event_type: str):
    type: Type[Daemon] = mapping.get(type, None)
    if not type:
        return "No such daemon type", 400

    event_type: Type[EventGroup] = type.mapping.get(event_type, None)
    if not event_type:
        return f"No such event type for {type}", 400
    return ",".join(event_type.mapping.keys())


@app.route("/daemon", methods=["POST"])
@fields(request)
def new_daemon(type: str, event_type: str, event: str, context_variable: str):

    type: Type[Daemon] = mapping.get(type, None)
    if not type:
        return "No such daemon type", 400

    event_type: Type[EventGroup] = type.mapping.get(event_type, None)
    if not event_type:
        return f"No such event type for {type}", 400

    event: Type[Event] = event_type.mapping.get(event, None)
    if not event:
        return f"No such event for event type {event_type}", 400

    daemon_manager + type(event_type, event, context_variable)
    print(daemon_manager.daemons)
    print(type, event_type, event, context_variable)
    return "Ok"


if __name__ == "__main__":

    with app.test_request_context():
        print(url_for("new_daemon"))
    daemon_manager = Daemonizer()
    app.run()
