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
    return Vlans(['primary'], ['secondary'])


def test_vlans_init(vlans):
    assert vlans.primary_vlans == ['primary']
    assert vlans.secondary_vlans == ['secondary']
    assert isinstance(vlans.interface, Interface)


def test_vlans_prepare(vlans, data):
    vlans.prepare()
    assert vlans.primary_vlans == [data[0], data[2], data[1], data[3]]


def test_vlans_prepare_secondaries(vlans, data):
    vlans.prepare()
    assert vlans.secondary_vlans == [data[5], data[4]]


def test_vlans_assign(vlans):
    vlans = Vlans([{'id': 0, 'device': 0}], [])
    vlan = vlans.book()
    assert vlan == {'id': 0, 'device': 0}
    assert vlans.primary_vlans == []


def test_vlans_assign_redundant(vlans):
    vlans = Vlans([{'id': 0, 'device': 0}], [{'id': 0, 'device': 0}])
    vlan = vlans.book(redundant=True)
    assert vlan == {'id': 0, 'device': 0}
    assert vlans.primary_vlans == []
    assert vlans.secondary_vlans == []


def test_vlans_assign_redundant_not_first(vlans):
    vlans = Vlans(
        [{'id': 0, 'device': 0}, {'id': 1, 'device': 0}],
        [{'id': 1, 'device': 0}]
    )
    vlan = vlans.book(redundant=True)
    assert vlan == {'id': 1, 'device': 0}
    assert vlans.primary_vlans == [{'id': 0, 'device': 0}]
    assert vlans.secondary_vlans == []
