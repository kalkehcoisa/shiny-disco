# -*- coding: utf-8 -*-
import csv


class Interface:
    """
    A CSV interface that allows to perform operations on csv files.
    """

    def __init__(self, filename):
        self.read(filename)

    def read(self, filename):
        csv.reader(filename)

    def write(self, data):
        self.data = True
