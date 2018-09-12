# Stubs for gunicorn.workers.gthread (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from . import base
from ..http import wsgi
from typing import Any

class TConn:
    cfg: Any = ...
    sock: Any = ...
    client: Any = ...
    server: Any = ...
    timeout: Any = ...
    parser: Any = ...
    def __init__(self, cfg: Any, sock: Any, client: Any, server: Any) -> None: ...
    def init(self) -> None: ...
    def set_timeout(self) -> None: ...
    def close(self) -> None: ...

class ThreadWorker(base.Worker):
    worker_connections: Any = ...
    max_keepalived: Any = ...
    tpool: Any = ...
    poller: Any = ...
    futures: Any = ...
    nr_conns: int = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @classmethod
    def check_config(cls, cfg: Any, log: Any) -> None: ...
    def init_process(self) -> None: ...
    alive: bool = ...
    def handle_quit(self, sig: Any, frame: Any) -> None: ...
    def enqueue_req(self, conn: Any) -> None: ...
    def accept(self, server: Any, listener: Any) -> None: ...
    def reuse_connection(self, conn: Any, client: Any): ...
    def murder_keepalived(self) -> None: ...
    def is_parent_alive(self): ...
    def run(self) -> None: ...
    def finish_request(self, fs: Any): ...
    def handle(self, conn: Any): ...
    def handle_request(self, req: Any, conn: Any): ...
