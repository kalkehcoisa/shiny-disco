# -*- coding: utf-8 -*-
from pytest import fixture

from shinydisco.Interface import Interface
from shinydisco.Vlans import Vlans


@fixture
def data():
    return [
        {'device_id': '0', 'primary_port': '1', 'vlan_id': '0'},
        {'device_id': '0', 'primary_port': '1', 'vlan_id': '1'},
        {'device_id': '1', 'primary_port': '1', 'vlan_id': '0'},
        {'device_id': '1', 'primary_port': '1', 'vlan_id': '1'},
        {'device_id': '0', 'primary_port': '0', 'vlan_id': '1'},
        {'device_id': '1', 'primary_port': '0', 'vlan_id': '0'}
    ]


@fixture
def vlans(mocker, data):
    mocker.patch.object(Interface, 'read')
    Interface.data = data
    return Vlans('filename')


@fixture
def prepared_vlans(vlans, data):
    vlans.primary_vlans = [data[0], data[2], data[1], data[3]]
    vlans.secondary_vlans = [data[5], data[4]]
    return vlans


def test_vlans(vlans):
    assert Interface.read.call_count == 1
    assert isinstance(vlans.interface, Interface)


def test_vlans_prepare(vlans, data):
    vlans.prepare()
    assert vlans.primary_vlans == [data[0], data[2], data[1], data[3]]


def test_vlans_prepare_secondaries(vlans, data):
    vlans.prepare()
    assert vlans.secondary_vlans == [data[5], data[4]]


def test_vlans_book(prepared_vlans, data):
    vlan = prepared_vlans.book()
    assert vlan == data[0]
    assert prepared_vlans.primary_vlans == [data[2], data[1], data[3]]


def test_vlans_book_redundant(prepared_vlans, data):
    vlan = prepared_vlans.book(redundant=True)
    assert vlan == data[2]
    assert prepared_vlans.primary_vlans == [data[0], data[1], data[3]]
    assert prepared_vlans.secondary_vlans == [data[4]]
