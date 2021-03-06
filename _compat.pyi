# Stubs for gunicorn._compat (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

PY26: Any
PY33: Any

def execfile_(fname: Any, *args: Any): ...
def bytes_to_str(b: Any): ...
def unquote_to_wsgi_str(string: Any): ...

unquote_to_wsgi_str: Any
BlockingIOError: Any
BrokenPipeError: Any
ChildProcessError: Any
ConnectionRefusedError: Any
ConnectionResetError: Any
InterruptedError: Any
ConnectionAbortedError: Any
PermissionError: Any
FileNotFoundError: Any
ProcessLookupError: Any

def wrap_error(func: Any, *args: Any, **kw: Any): ...

class BlockingIOError(OSError): ...
class BrokenPipeError(OSError): ...
class ChildProcessError(OSError): ...
class ConnectionRefusedError(OSError): ...
class InterruptedError(OSError): ...
class ConnectionResetError(OSError): ...
class ConnectionAbortedError(OSError): ...
class PermissionError(OSError): ...
class FileNotFoundError(OSError): ...
class ProcessLookupError(OSError): ...

def urlsplit(url: Any, scheme: str = ..., allow_fragments: bool = ...): ...

positionals: Any

def get_arity(f: Any): ...
def html_escape(s: Any): ...
