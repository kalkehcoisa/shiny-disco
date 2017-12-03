# -*- coding: utf-8 -*-
import csv

from pytest import fixture

from shinydisco.Interface import Interface


@fixture
def interface(mocker):
    mocker.patch.object(Interface, 'read')
    return Interface('mycsv.csv')


def test_interface(interface):
    Interface.read.assert_called_with('mycsv.csv')


def test_interface_read(mocker):
    mocker.patch.object(csv, 'reader')
    interface = Interface('mycsv.csv')
    interface.read('mycsv.csv')
    csv.reader.assert_called_with('mycsv.csv')


def test_interface_write(interface):
    interface.write({})
    assert interface.data
