import time
import inspect


class SpeedProfiler:
    def __init__(self, identifier):
        line_num = inspect.currentframe().f_back.f_lineno
        self.laps = []
        self.lap_results = []
        self.laps.append({
            'identifier': identifier,
            'time': time.perf_counter(),
            'line_num': line_num
        })

    def mark(self, identifier):
        line_num = inspect.currentframe().f_back.f_lineno
        self.laps.append({
            'identifier': identifier,
            'time': time.perf_counter(),
            'line_num': line_num
        })

    def stop(self):
        line_num = inspect.currentframe().f_back.f_lineno
        self.laps.append({
            'identifier': '',
            'time': time.perf_counter(),
            'line_num': line_num
        })
        total_time = self.laps[len(self.laps) - 1]['time'] - self.laps[0]['time']
        even = False
        i = 0
        for lap in self.laps:
            if i== 0:
                i += 1
                continue
            elapsed = lap['time'] - self.laps[i - 1]['time']
            self.lap_results.append({
                'identifier': self.laps[i - 1]['identifier'],
                'duration': elapsed,
                'percent_time': round(self.percentage(elapsed, total_time), 2),
                'line_num': self.laps[i - 1]['line_num']
            })
            i += 1
            even = not even

        return self.lap_results

    def percentage(self, part, whole):
        return (part / whole) * 100.0


# Global scope profiler
if globals().get('speed_profiler', None) is None:
    speed_profiler = SpeedProfiler('GLOBAL')
