# Stubs for gunicorn.workers.base (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class Worker:
    SIGNALS: Any = ...
    PIPE: Any = ...
    age: Any = ...
    pid: str = ...
    ppid: Any = ...
    sockets: Any = ...
    app: Any = ...
    timeout: Any = ...
    cfg: Any = ...
    booted: bool = ...
    aborted: bool = ...
    reloader: Any = ...
    nr: int = ...
    max_requests: Any = ...
    alive: bool = ...
    log: Any = ...
    tmp: Any = ...
    def __init__(self, age: Any, ppid: Any, sockets: Any, app: Any, timeout: Any, cfg: Any, log: Any) -> None: ...
    def notify(self) -> None: ...
    def run(self) -> None: ...
    wait_fds: Any = ...
    def init_process(self) -> None: ...
    wsgi: Any = ...
    def load_wsgi(self) -> None: ...
    def init_signals(self) -> None: ...
    def handle_usr1(self, sig: Any, frame: Any) -> None: ...
    def handle_exit(self, sig: Any, frame: Any) -> None: ...
    def handle_quit(self, sig: Any, frame: Any) -> None: ...
    def handle_abort(self, sig: Any, frame: Any) -> None: ...
    def handle_error(self, req: Any, client: Any, addr: Any, exc: Any) -> None: ...
    def handle_winch(self, sig: Any, fname: Any) -> None: ...
