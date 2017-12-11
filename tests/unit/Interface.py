# -*- coding: utf-8 -*-
import csv
import os
from unittest.mock import ANY

from pytest import fixture

from shinydisco.Interface import Interface


@fixture
def csvfile(csv_teardown):
    with open('testcsv.csv', 'w') as csvfile:
        csvfile.close()


@fixture
def interface(mocker):
    return Interface('testcsv.csv')


def test_interface(interface):
    interface.filename == 'testcsv.csv'


def test_interface_path(mocker, interface):
    mocker.patch('os.path.join')
    result = interface.path()
    os.path.join.assert_called_with(os.getcwd(), interface.filename)
    assert result == os.path.join()


def test_interface_read(mocker, interface, csvfile):
    mocker.patch.object(Interface, 'path')
    mocker.patch.object(csv, 'DictReader')
    interface.read()
    assert interface.path.call_count == 1
    assert interface.data == csv.DictReader()


def test_interface_write(mocker, interface, csvfile):
    mocker.patch.object(Interface, 'path')
    mocker.patch.object(csv, 'DictWriter')
    interface.write(['headers'], [{}])
    csv.DictWriter.assert_called_with(ANY, fieldnames=['headers'])
    csv.DictWriter().writerow.assert_called_with({})
    assert interface.path.call_count == 1
    assert csv.DictWriter().writeheader.call_count == 1
