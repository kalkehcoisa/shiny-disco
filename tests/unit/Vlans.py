# -*- coding: utf-8 -*-
from shinydisco.Vlans import Vlans


def test_vlans_init():
    vlans = Vlans(['primary'], ['secondary'])
    assert vlans.primary_vlans == ['primary']
    assert vlans.secondary_vlans == ['secondary']


def test_vlans_assign():
    vlans = Vlans([{'id': 0, 'device': 0}], [])
    vlan = vlans.book()
    assert vlan == {'id': 0, 'device': 0}
    assert vlans.primary_vlans == []


def test_vlans_assign_redundant():
    vlans = Vlans([{'id': 0, 'device': 0}], [{'id': 0, 'device': 0}])
    vlan = vlans.book(redundant=True)
    assert vlan == {'id': 0, 'device': 0}
    assert vlans.primary_vlans == []
    assert vlans.secondary_vlans == []


def test_vlans_assign_redundant_not_first():
    vlans = Vlans(
        [{'id': 0, 'device': 0}, {'id': 1, 'device': 0}],
        [{'id': 1, 'device': 0}]
    )
    vlan = vlans.book(redundant=True)
    assert vlan == {'id': 1, 'device': 0}
    assert vlans.primary_vlans == [{'id': 0, 'device': 0}]
    assert vlans.secondary_vlans == []
