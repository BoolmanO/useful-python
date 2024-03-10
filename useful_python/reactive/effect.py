from useful_python.reactive.protocols.observer import ObserverProtocol


def effect(fn) -> ObserverProtocol:
    """
    A function to turn a function into an "effect". The same function, but implementing the __push__ method, which is required by the Observer protocol.

    :param fn: Callable object.
    :returns: Same function as fn that can be used as Observer

    .. code-block:: python

        def log(observer, name, value) -> None:
            print(observer, name, value)


        class Cache(ObservableChanges):
            observers = [effect(log)]

    effect doesn't working with builtin functions, use lambda instead.
    """
    fn.__push__ = fn.__call__
    return fn
