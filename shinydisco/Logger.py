# -*- coding: utf-8 -*-
import logging


class Logger:
    """
    Wraps the standard logger to make it more accessible from other classes.
    """

    verbosities = ['critical', 'error', 'warning', 'info', 'debug']
    events = {
        'run-verbosity': ('debug', 'Running with verbosity level {}'),
        'book-vlan': ('info', 'Booked vlan id {}, device {}, redudancy {}')
    }

    def __init__(self, *args, verbosity=0, output='stdout'):
        level = self._level_from_verbosity(verbosity)
        self.start_logger(level)
        self.add_handler(level, output)

    def _level_from_verbosity(self, verbosity):
        if verbosity >= len(self.verbosities):
            verbosity = len(self.verbosities) - 1
        return getattr(logging, self.verbosities[verbosity].upper())

    def start_logger(self, level):
        logging.basicConfig(level=level)
        self.logger = logging.getLogger('shinydisco')

    def add_handler(self, level, output):
        if output != 'stdout':
            handler = logging.FileHandler(output)
            handler.setLevel(level)
            self.logger.addHandler(handler)

    def log(self, event, *args):
        message = event
        level = logging.INFO
        if event in self.events:
            level = getattr(logging, self.events[event][0].upper())
            message = self.events[event][1]
        self.logger.log(level, message.format(*args))
