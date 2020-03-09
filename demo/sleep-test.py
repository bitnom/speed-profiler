from speed_profiler import SpeedProfiler
from time import sleep
from pprint import pprint

sp = SpeedProfiler('Sleep Tester')


def foo():
    sleep(0.2)
    sp.mark('Foo')


def bar():
    sleep(0.1)
    sp.mark('bar')


def baz():
    foo()
    bar()
    sp.mark('baz')
    profile = sp.stop()
    pprint(profile)


baz()
