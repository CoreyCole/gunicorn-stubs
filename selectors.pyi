# Stubs for gunicorn.selectors (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import Mapping, namedtuple
from typing import Any, Optional

EVENT_READ: Any
EVENT_WRITE: Any

SelectorKey = namedtuple('SelectorKey', ['fileobj', 'fd', 'events', 'data'])

class _SelectorMapping(Mapping):
    def __init__(self, selector: Any) -> None: ...
    def __len__(self): ...
    def __getitem__(self, fileobj: Any): ...
    def __iter__(self): ...

class BaseSelector:
    def register(self, fileobj: Any, events: Any, data: Optional[Any] = ...) -> None: ...
    def unregister(self, fileobj: Any) -> None: ...
    def modify(self, fileobj: Any, events: Any, data: Optional[Any] = ...): ...
    def select(self, timeout: Optional[Any] = ...) -> None: ...
    def close(self) -> None: ...
    def get_key(self, fileobj: Any): ...
    def get_map(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args: Any) -> None: ...

class _BaseSelectorImpl(BaseSelector):
    def __init__(self) -> None: ...
    def register(self, fileobj: Any, events: Any, data: Optional[Any] = ...): ...
    def unregister(self, fileobj: Any): ...
    def modify(self, fileobj: Any, events: Any, data: Optional[Any] = ...): ...
    def close(self) -> None: ...
    def get_map(self): ...

class SelectSelector(_BaseSelectorImpl):
    def __init__(self) -> None: ...
    def register(self, fileobj: Any, events: Any, data: Optional[Any] = ...): ...
    def unregister(self, fileobj: Any): ...
    def select(self, timeout: Optional[Any] = ...): ...

class PollSelector(_BaseSelectorImpl):
    def __init__(self) -> None: ...
    def register(self, fileobj: Any, events: Any, data: Optional[Any] = ...): ...
    def unregister(self, fileobj: Any): ...
    def select(self, timeout: Optional[Any] = ...): ...

class EpollSelector(_BaseSelectorImpl):
    def __init__(self) -> None: ...
    def fileno(self): ...
    def register(self, fileobj: Any, events: Any, data: Optional[Any] = ...): ...
    def unregister(self, fileobj: Any): ...
    def select(self, timeout: Optional[Any] = ...): ...
    def close(self) -> None: ...

class DevpollSelector(_BaseSelectorImpl):
    def __init__(self) -> None: ...
    def fileno(self): ...
    def register(self, fileobj: Any, events: Any, data: Optional[Any] = ...): ...
    def unregister(self, fileobj: Any): ...
    def select(self, timeout: Optional[Any] = ...): ...
    def close(self) -> None: ...

class KqueueSelector(_BaseSelectorImpl):
    def __init__(self) -> None: ...
    def fileno(self): ...
    def register(self, fileobj: Any, events: Any, data: Optional[Any] = ...): ...
    def unregister(self, fileobj: Any): ...
    def select(self, timeout: Optional[Any] = ...): ...
    def close(self) -> None: ...
DefaultSelector = KqueueSelector
DefaultSelector = EpollSelector
DefaultSelector = DevpollSelector
DefaultSelector = PollSelector
DefaultSelector = SelectSelector
