# speed-profiler

Accurate speed profiler for Python code using perf_counter.

This module is for finding bottlenecks in Python code. The first call to the module
initializes it with a name to identify the profile. Following that are calls to `mark()`
for timing purposes. Here's an example (Also in the demo folder):

## Installation
`pip install speed-profiler`

## Usage
```
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

```

*Output*:
```
[{'duration': 0.20027251401916146,
  'identifier': 'Sleep Tester',
  'line_num': 5,
  'percent_time': 66.66},
 {'duration': 0.10016519500641152,
  'identifier': 'Foo',
  'line_num': 10,
  'percent_time': 33.34},
 {'duration': 1.0420975740998983e-05,
  'identifier': 'bar',
  'line_num': 15,
  'percent_time': 0.0},
 {'duration': 9.390001650899649e-06,
  'identifier': 'baz',
  'line_num': 21,
  'percent_time': 0.0}]
```