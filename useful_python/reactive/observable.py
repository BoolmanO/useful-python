from __future__ import annotations

from typing import Any, Iterable

from useful_python.reactive.protocols.observable import (
    BaseObservableProtocol,
    ObservableChangesProtocol,
)
from useful_python.reactive.protocols.observer import ObserverProtocol


class Observable(BaseObservableProtocol):
    """Implement only `self.push` method."""

    observers: Iterable[ObserverProtocol] = []

    def __init__(self, observers: Iterable[ObserverProtocol] | None = None):
        if self.observers == []:
            if observers is None:
                observers = []
            self.observers = observers

    def push(self, name: Any, value: Any) -> None:
        """
        Notify all observers that the state of `name` was changed to `value`.

        :param name: `name` of state. Can be index or key.
        :param value: new `value` of state.
        """
        for observer in self.observers:
            observer.__push__(self, name, value)


class ObservableChanges(Observable, ObservableChangesProtocol):
    """Implement `self.push` method, and call it automatically when the __setattr__ is called."""

    def __setattr__(self, __name: Any, __value: Any) -> None:
        self.push(__name, __value)
        self.__dict__[__name] = __value


class ObservableDict(ObservableChanges, dict):
    """Implement `self.push` method, and call it automatically when dictionary state is changed."""

    observers: Iterable[ObserverProtocol] = []

    def __setitem__(self, __key: Any, __value: Any) -> None:
        self.push(__key, __value)
        return super().__setitem__(__key, __value)

    @staticmethod
    def from_dict(
        dictionary: dict, observers: Iterable[ObserverProtocol] | None = None
    ) -> ObservableDict:
        """
        Create ObservableDict from builtin dict.

        :param dictionary: origin dict.
        :param observers: iterable (FE: list or tuple) with observers.
        :returns: observable dict with origin dict data.
        """
        if observers is None:
            observers = []

        obs_dict = ObservableDict()
        obs_dict.update(dictionary)
        obs_dict.observers = observers
        return obs_dict


# TODO: Add ObservableList, ObservableTuple
