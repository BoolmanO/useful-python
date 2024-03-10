from __future__ import annotations

from typing import Any, Protocol

from useful_python.reactive.protocols.observable import BaseObservableProtocol


class ObserverProtocol(Protocol):
    """Observer protocol."""

    def __push__(
        self, observable: BaseObservableProtocol, name: Any, value: Any
    ) -> Any:
        pass
