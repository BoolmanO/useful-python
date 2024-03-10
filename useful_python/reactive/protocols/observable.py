from __future__ import annotations

from typing import Any, Iterable, Protocol

from useful_python.reactive.protocols.observer import ObserverProtocol


class BaseObservableProtocol(Protocol):
    """Base protocol for observable."""

    observers: Iterable[ObserverProtocol]


class ObservableChangesProtocol(BaseObservableProtocol):
    """Protocol for observable changes of class."""

    def __setattr__(self, __name: Any, __value: Any) -> None:
        pass
