# -*- coding: utf-8 -*-
import csv
from collections import OrderedDict

from pytest import fixture

from shinydisco.Interface import Interface


@fixture
def testcsv(csv_teardown):
    with open('testcsv.csv', 'w+') as testcsv:
        header = ['request_id', 'redundant']
        writer = csv.DictWriter(testcsv, fieldnames=header)
        writer.writeheader()
        writer.writerow({'request_id': '1', 'redundant': '0'})


def test_interface_read(testcsv):
    interface = Interface('testcsv.csv')
    interface.read()
    data = list(i for i in interface.data)
    assert data == [OrderedDict([('request_id', '1'), ('redundant', '0')])]
