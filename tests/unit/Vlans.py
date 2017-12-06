# -*- coding: utf-8 -*-
from shinydisco.Vlans import Vlans


def test_vlans_init():
    vlans = Vlans(['primary'], ['secondary'])
    assert vlans.primary_vlans == ['primary']
    assert vlans.secondary_vlans == ['secondary']


def test_vlans_assign():
    vlans = Vlans([{'id': 0, 'device': 0}], [])
    vlan = vlans.assign()
    assert vlan == {'id': 0, 'device': 0}
    assert vlans.primary_vlans == []


def test_vlans_assign_redundant():
    vlans = Vlans([{'id': 0, 'device': 0}], [{'id': 0, 'device': 0}])
    vlan = vlans.assign(redundant=True)
    assert vlan == {'id': 0, 'device': 0}
    assert vlans.primary_vlans == []
    assert vlans.secondary_vlans == []
