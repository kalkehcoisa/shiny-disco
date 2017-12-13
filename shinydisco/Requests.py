# -*- coding: utf-8 -*-
from .Interface import Interface


class Requests:
    """
    Model for requests
    """

    def __init__(self, path):
        self.interface = Interface(path)
        self.interface.read()

    def get(self):
        return self.interface.data
