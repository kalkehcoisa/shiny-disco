# -*- coding: utf-8 -*-
import csv
import os

from pytest import fixture

from shinydisco.Interface import Interface


@fixture
def csv_teardown(request):
    def teardown():
        os.remove('mycsv.csv')
    request.addfinalizer(teardown)


@fixture
def csvfile(csv_teardown):
    with open('mycsv.csv', 'w') as csvfile:
        csvfile.close()


@fixture
def interface(mocker):
    return Interface('mycsv.csv')


def test_interface(interface):
    interface.filename == 'mycsv.csv'


def test_interface_read(mocker, interface, csvfile):
    mocker.patch('os.path.join')
    mocker.patch('csv.DictReader')
    interface.read()
    os.path.join.assert_called_with(os.getcwd(), 'mycsv.csv')
    assert interface.data == csv.DictReader()


def test_interface_write(interface):
    interface.write({})
    assert interface.data
