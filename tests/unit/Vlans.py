# -*- coding: utf-8 -*-
from pytest import fixture, mark

from shinydisco.Interface import Interface
from shinydisco.Vlans import Vlans


@fixture
def data():
    return [
        {'device_id': '0', 'primary_port': '1', 'vlan_id': '0'},
        {'device_id': '0', 'primary_port': '1', 'vlan_id': '2'},
        {'device_id': '5', 'primary_port': '1', 'vlan_id': '1'},
        {'device_id': '5', 'primary_port': '1', 'vlan_id': '3'},
        {'device_id': '0', 'primary_port': '0', 'vlan_id': '2'},
        {'device_id': '5', 'primary_port': '0', 'vlan_id': '1'}
    ]


@fixture
def vlans(mocker, data, logger):
    mocker.patch.object(Interface, 'read')
    Interface.data = data
    return Vlans('filename', logger)


@fixture
def prepared_vlans(vlans, data):
    vlans.primary_vlans = [data[0], data[2], data[1], data[3]]
    vlans.secondary_vlans = [data[5], data[4]]
    return vlans


def test_vlans(vlans, logger):
    assert Interface.read.call_count == 1
    assert vlans.logger == logger
    assert isinstance(vlans.interface, Interface)


def test_vlans_prepare(vlans, data):
    vlans.prepare()
    assert vlans.primary_vlans == [data[0], data[2], data[1], data[3]]


def test_vlans_prepare_secondaries(vlans, data):
    vlans.prepare()
    assert vlans.secondary_vlans == [data[5], data[4]]


def test_vlans_book(prepared_vlans, data):
    vlan = prepared_vlans.book(redundant='0')
    assert vlan == data[0]
    assert prepared_vlans.primary_vlans == [data[2], data[1], data[3]]


def test_vlans_book_redundant(prepared_vlans, data):
    vlan = prepared_vlans.book(redundant='1')
    assert vlan == data[2]
    assert prepared_vlans.primary_vlans == [data[0], data[1], data[3]]
    assert prepared_vlans.secondary_vlans == [data[4]]


@mark.parametrize('redundant, index', [('0', 0), ('1', 2)])
def test_vlans_book_log(prepared_vlans, data, logger, redundant, index):
    prepared_vlans.book(redundant=redundant)
    vlan = data[index]
    args = [vlan['vlan_id'], vlan['device_id'], redundant]
    logger.log.assert_called_with('book-vlan', *args)
