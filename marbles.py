from rx.testing import marbles
from rx import Observable, Observer


xs = Observable.from_marbles("a-b-c-|")
xs.to_blocking().to_marbles()

