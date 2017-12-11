# -*- coding: utf-8 -*-
import csv
import os


class Interface:
    """
    A CSV interface that allows to perform operations on csv files.
    """

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        filepath = os.path.join(os.getcwd(), self.filename)
        with open(filepath, 'r') as csvfile:
            self.data = csv.reader(csvfile)

    def write(self, data):
        self.data = True
