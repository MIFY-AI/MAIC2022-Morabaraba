import time

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:

    timers = dict()    
    def __init__(self, name=None, total_time = 50.0, text="Elapsed time: {:0.4f} seconds", logger=print):
        self._start_time = None
        self.name = name
        self.text = text
        self.logger = logger
        self.total_time = total_time

        # Add new named timers to dictionary of timers
        if name:
            self.timers.setdefault(name, 0)

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def reset(self):
        self.timers[self.name] = 0

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(self.text.format(elapsed_time))

        if self.logger:
            self.logger(self.text.format(elapsed_time))

        if self.name:
            self.timers[self.name] += elapsed_time

        return elapsed_time

    def remain_time(self):
        return self.total_time - self.timers[self.name]