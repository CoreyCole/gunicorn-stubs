# Stubs for gunicorn.glogging (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

SYSLOG_FACILITIES: Any
CONFIG_DEFAULTS: Any

def loggers(): ...

class SafeAtoms(dict):
    def __init__(self, atoms: Any) -> None: ...
    def __getitem__(self, k: Any): ...

def parse_syslog_address(addr: Any): ...

class Logger:
    LOG_LEVELS: Any = ...
    loglevel: Any = ...
    error_fmt: str = ...
    datefmt: str = ...
    access_fmt: str = ...
    syslog_fmt: str = ...
    atoms_wrapper_class: Any = ...
    error_log: Any = ...
    access_log: Any = ...
    error_handlers: Any = ...
    access_handlers: Any = ...
    logfile: Any = ...
    lock: Any = ...
    cfg: Any = ...
    def __init__(self, cfg: Any) -> None: ...
    def setup(self, cfg: Any) -> None: ...
    def critical(self, msg: Any, *args: Any, **kwargs: Any) -> None: ...
    def error(self, msg: Any, *args: Any, **kwargs: Any) -> None: ...
    def warning(self, msg: Any, *args: Any, **kwargs: Any) -> None: ...
    def info(self, msg: Any, *args: Any, **kwargs: Any) -> None: ...
    def debug(self, msg: Any, *args: Any, **kwargs: Any) -> None: ...
    def exception(self, msg: Any, *args: Any, **kwargs: Any) -> None: ...
    def log(self, lvl: Any, msg: Any, *args: Any, **kwargs: Any) -> None: ...
    def atoms(self, resp: Any, req: Any, environ: Any, request_time: Any): ...
    def access(self, resp: Any, req: Any, environ: Any, request_time: Any): ...
    def now(self): ...
    def reopen_files(self) -> None: ...
    def close_on_exec(self) -> None: ...
