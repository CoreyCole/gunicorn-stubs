# Stubs for gunicorn.instrument.statsd (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from gunicorn.glogging import Logger
from typing import Any

METRIC_VAR: str
VALUE_VAR: str
MTYPE_VAR: str
GAUGE_TYPE: str
COUNTER_TYPE: str
HISTOGRAM_TYPE: str

class Statsd(Logger):
    prefix: Any = ...
    sock: Any = ...
    def __init__(self, cfg: Any) -> None: ...
    def critical(self, msg: Any, *args: Any, **kwargs: Any) -> None: ...
    def error(self, msg: Any, *args: Any, **kwargs: Any) -> None: ...
    def warning(self, msg: Any, *args: Any, **kwargs: Any) -> None: ...
    def exception(self, msg: Any, *args: Any, **kwargs: Any) -> None: ...
    def info(self, msg: Any, *args: Any, **kwargs: Any) -> None: ...
    def debug(self, msg: Any, *args: Any, **kwargs: Any) -> None: ...
    def log(self, lvl: Any, msg: Any, *args: Any, **kwargs: Any) -> None: ...
    def access(self, resp: Any, req: Any, environ: Any, request_time: Any) -> None: ...
    def gauge(self, name: Any, value: Any) -> None: ...
    def increment(self, name: Any, value: Any, sampling_rate: float = ...) -> None: ...
    def decrement(self, name: Any, value: Any, sampling_rate: float = ...) -> None: ...
    def histogram(self, name: Any, value: Any) -> None: ...
