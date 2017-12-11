# -*- coding: utf-8 -*-
import csv
import os


class Interface:
    """
    A CSV interface that allows to perform operations on csv files.
    """

    def __init__(self, filename):
        self.filename = filename

    def path(self):
        return os.path.join(os.getcwd(), self.filename)

    def read(self):
        with open(self.path(), 'r') as csvfile:
            self.data = csv.DictReader(csvfile)

    def write(self, headers, data):
        with open(self.path(), 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader(headers)
            for item in data:
                writer.writerow(item)
