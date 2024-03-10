"""Package with protocols for creating Observer-Observable relationships."""

from .observable import BaseObservableProtocol, ObservableChangesProtocol
from .observer import ObserverProtocol

__all__ = ["BaseObservableProtocol", "ObservableChangesProtocol", "ObserverProtocol"]
